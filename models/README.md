# Models

Directory for saving trained models to.

## RestAI_model_v1.pkl

Final model for this project during the midterm project of ML Zoomcamp 2024.
It is the first finalized (and so far only) version of the model, so it is
versioned using the suffix `v1. This is the model deployed in the application.

Model selection and evaluation was done in the notebook
`02-train_evaluate_compare_models.ipynb`.
This final model was trained in the script `train.py`.
Train and test data is in the directory `data/processed/main`.
RMSE on test set: 0.3294.

## Models for Data Processing

- `dict_vectorizer.pkl`: DictVectorizer for one-hot encoding
- `scaler_features.pkl`: MinMaxScaler for normalizing features
- `scaler_label.pkl`: MinMaxScaler for normalizing label

They were fit in the notebook `01-data_preparation.ipynb`.

`dict_vectorizer.pkl` and `scaler_features.pkl` are used in the
script for deployment using flask `predict.py`.
