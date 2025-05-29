import axios from 'axios';

export const uploadDatasetAndTrain = async (formData: FormData) => {
  return axios.post('http://localhost:8000/train', formData, {
    responseType: 'blob',
  });
};
