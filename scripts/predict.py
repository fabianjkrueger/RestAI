##### goal: deploy model in flask and make API endpoints for inference #####

## preparations

# dependencies
import pandas as pd
from joblib import load
from pathlib import Path

from flask import Flask
from flask import request
from flask import jsonify

# paths
PATH_MODELS = Path(__file__).parent.parent / "models"
PATH_MODEL = PATH_MODELS / "RestAI_model_v1.pkl"
PATH_DICT_VECTORIZER = PATH_MODELS / "dict_vectorizer.pkl"
PATH_SCALER = PATH_MODELS / "scaler_features.pkl"

# load final model
model = load(PATH_MODEL)

# load dict vectorizer and scaler
dict_vectorizer = load(PATH_DICT_VECTORIZER)
scaler = load(PATH_SCALER)

# define categorical and numerical columns


## build flask backend app with API endpoints

# initialize flask app
app = Flask("RestAI")

# define API endpoint for inference on untransformed data
# here untransformed means: neither one hot encoded, nor scaled
@app.route("/predict_untransformed", methods=["POST"])
def predict_untransformed():
    
    # get data from request
    data = request.get_json()
    
    # one hot encode data
    X_encoded = dict_vectorizer.transform(data)
    
    # get feature names in correct order from dict vectorizer
    feature_names = dict_vectorizer.get_feature_names_out()
    
    # convert to DataFrame and assign colnames
    # dict vectorizer returns matrix
    # drop sleep_quality column to get features only
    # it is added by dict vectorizer
    df = pd.DataFrame(
        X_encoded,
        columns=feature_names
    ).drop(columns="sleep_quality")
    
    # get numerical columns for scaling
    num_cols = [
        "age",
        "study_hours",
        "screen_time",
        "caffeine_intake",
        "physical_activity",
        "bedtime",
        "wakeup_time"
    ]
    
    # scale data
    df[num_cols] = scaler.transform(df[num_cols])

    # make prediction
    sleep_quality = model.predict(df)
    
    # construct json response
    response = {
        "sleep_quality": sleep_quality.tolist()
    }
    
    return jsonify(response)

# define API endpoint for inference with transformed data
# here transformed means: one hot encoded and normalized
@app.route("/predict_transformed", methods=["POST"])
def predict_transformed():
    # get data from request
    data = request.get_json()
    
    print(data)
    
    # convert dictionary to DataFrame
    # wrap data in list to create single row DataFrame
    df = pd.DataFrame([data])
    
    print(df)
    
    # make prediction
    sleep_quality = model.predict(df)
    
    # construct json response
    response = {
        "sleep_quality": sleep_quality.tolist()
    }
    
    return jsonify(response)

# main method to only run the app if this script is explicitly called
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=9696
    )





