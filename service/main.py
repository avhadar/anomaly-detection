from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# define the request model for API predictions
class PredictionRequest(BaseModel):
    feature_vector: List[float]
    score: Optional[bool] = None

# create the API object
app = FastAPI()

# load the IsolationForest model
model = joblib.load("isoforest.joblib")

# define the endpoints
@app.get("/model_information")
def model_info():
    return model.get_params()

@app.post("/prediction")
def make_prediction(request: PredictionRequest):
    response = dict()
    feature_vector = request.feature_vector
    response["is_inlier"] = int( model.predict([feature_vector])[0] )
    if request.score:
        response["anomaly_score"] = float( model.score_samples([feature_vector])[0] )
    return response



