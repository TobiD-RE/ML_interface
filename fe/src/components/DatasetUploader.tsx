import React, { useState } from 'react';

interface Props {
  onTrain: (request: FormData) => void;
}

const DatasetUploader: React.FC<Props> = ({ onTrain }) => {
  const [datasetSource, setDatasetSource] = useState<'upload' | 'url'>('upload');
  const [file, setFile] = useState<File | null>(null);
  const [url, setUrl] = useState<string>('');

  const handleTrain = () => {
    const formData = new FormData();
    formData.append('datasetSource', datasetSource);
    if (datasetSource === 'upload' && file) {
      formData.append('datasetFile', file);
    } else if (datasetSource === 'url') {
      formData.append('datasetUrl', url);
    }
    formData.append('algorithm', 'placeholder-algo');
    onTrain(formData);
  };

  return (
    <div>
      <h3>Dataset Input</h3>
      <div>
        <label>
          <input
            type="radio"
            value="upload"
            checked={datasetSource === 'upload'}
            onChange={() => setDatasetSource('upload')}
          />
          Upload CSV
        </label>
        <label>
          <input
            type="radio"
            value="url"
            checked={datasetSource === 'url'}
            onChange={() => setDatasetSource('url')}
          />
          Provide URL
        </label>
      </div>

      {datasetSource === 'upload' ? (
        <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files?.[0] || null)} />
      ) : (
        <input type="text" placeholder="https://example.com/data.csv" value={url} onChange={(e) => setUrl(e.target.value)} />
      )}

      <button onClick={handleTrain}>Train Model</button>
    </div>
  );
};

export default DatasetUploader;
