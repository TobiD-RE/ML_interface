export type DatasetSource = 'upload' | 'url';

export interface TrainRequest {
  datasetSource: DatasetSource;
  datasetFile?: File;
  datasetUrl?: string;
  algorithm: string; // placeholder
}
