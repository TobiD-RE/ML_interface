import React, { useState } from 'react';
import DatasetUploader from './components/DatasetUploader';
import AlgorithmSelector from './components/AlgorithmSelector';
import { uploadDatasetAndTrain } from './api';

const App: React.FC = () => {
  const [downloadLink, setDownloadLink] = useState<string | null>(null);

  const handleTrain = async (formData: FormData) => {
    try {
      const response = await uploadDatasetAndTrain(formData);
      const blob = new Blob([response.data], { type: 'application/octet-stream' });
      const url = URL.createObjectURL(blob);
      setDownloadLink(url);
    } catch (error) {
      console.error('Training failed', error);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>ML Trainer Interface</h1>
      <AlgorithmSelector />
      <DatasetUploader onTrain={handleTrain} />

      {downloadLink && (
        <a href={downloadLink} download="model.pkl">
          Download Trained Model
        </a>
      )}
    </div>
  );
};

export default App;
