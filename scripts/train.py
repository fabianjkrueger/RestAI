##### goal: train final model and save it to a pickle file #####
# model selection and evaluation was done in notebook 
# `02-train_evaluate_compare_models.ipynb`

## preparations

print("Setting up workspace...")

# dependencies
from pathlib import Path
from joblib import dump
import pandas as pd

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import root_mean_squared_error

# paths
PATH_DATA = Path(__file__).parent.parent / "data/processed/main"
PATH_MODEL = Path(__file__).parent.parent / "models/RestAI_model_v1.pkl"

# load data

# train
X_train = pd.read_csv(PATH_DATA / "sleep_data_main_train_features.csv")
y_train = pd.read_csv(PATH_DATA / "sleep_data_main_train_labels.csv")

# test
X_test = pd.read_csv(PATH_DATA / "sleep_data_main_test_features.csv")
y_test = pd.read_csv(PATH_DATA / "sleep_data_main_test_labels.csv")

## train model

print("Initializing final model...")

# initialize final model
final_model = ExtraTreesRegressor(
    max_depth=3,
    max_features='sqrt',
    min_samples_leaf=4,
    min_samples_split=10,
    n_estimators=100,
    random_state=1337,
    n_jobs=-1
)

print(f"final_model: {final_model}")

print("Training final model...")

# fit the model on the training data
final_model.fit(X_train, y_train.squeeze())

## evaluate model

print("Evaluating final model...")

# get predictions of the model on the test set
y_pred = final_model.predict(X_test)

# calculate RMSE of final model using test set and predictions
test_rmse = root_mean_squared_error(y_test, y_pred)

print(f"RMSE on test set: {test_rmse:.4f}")

## save model

print(f"Saving final model to: {PATH_MODEL}")

# save model to pickle file
dump(final_model, PATH_MODEL)

print("Done!")








