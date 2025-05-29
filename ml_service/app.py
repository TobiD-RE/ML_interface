from flask import Flask, request, send_file, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
import requests
from io import BytesIO
from algorithms import ALGORITHM_MAP

app = Flask(__name__)

@app.route('/train-model/', methods=['POST'])
def train_model():
    dataset_source = request.form.get('datasetSource')
    dataset_url = request.form.get('datasetUrl')
    algorithm_key = request.form.get('algorithm')
    dataset_file = request.files.get('datasetFile')

    try:
        if dataset_source == 'upload' and dataset_file:
            df = pd.read_csv(dataset_file)
        elif dataset_source =='url' and dataset_url:
            response = request.get(dataset_url)
            df = pd.read_csv(BytesIO(response.content))
        else:
            return jsonify({'error': 'Missing dataset filoe or URL'}), 400
    except Exception as e:
        return jsonify({'error': f'Failed to load dataset: {str(e)}'}), 400
    
    model = ALGORITHM_MAP.get(algorithm_key)
    if model is None:
        return jsonify({'error': f'Invalid algorithm: {algorithm_key}. Supported: {list(ALGORITHM_MAP.keys())}'}), 400
    
    try:
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model.fit(X_train, y_train)

        model_path = 'model.pkl'
        joblib.dump(model, model_path)
    except Exception as e:
        return jsonify({'error': f'Training Failed: {str(e)}'}), 500
    
    return send_file(model_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)