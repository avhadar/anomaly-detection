from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import make_asgi_app, Counter, Histogram
import joblib
import time

# define the request model for API predictions
class PredictionRequest(BaseModel):
    feature_vector: List[float]
    score: Optional[bool] = None

# create the API object
app = FastAPI()

# create the ASGI object
metrics_app = make_asgi_app()
# mount the metrics_app at the metrics endpoint
app.mount('/metrics', metrics_app)

# create metrics: counters, histograms
# create counters
model_info_counter = Counter('model_info', 'Numer of calls to model_information')
prediction_counter = Counter('prediction', 'Numer of calls to prediction')
# create histograms
h_prediction = Histogram('prediction_response', 'Predicted values')
h_score_samples = Histogram('score_response', 'Score samples')
h_latency = Histogram('prediction_latency', 'Latency of prediction function')

# load the IsolationForest model
model = joblib.load("isoforest.joblib")

# define the endpoints
@app.get("/model_information")
def model_info():
    # update counter
    model_info_counter.inc() # increment by 1
    # return details about the model
    return model.get_params()


@app.post("/prediction")
def make_prediction(request: PredictionRequest):
    start = time.time()
    # update counter
    prediction_counter.inc() # increment by 1
    # generate response
    response = dict()
    feature_vector = request.feature_vector
    response["is_inlier"] = int( model.predict([feature_vector])[0] )
    # update histogram
    h_prediction.observe(response["is_inlier"])
    
    if request.score:
        response["anomaly_score"] = float( model.score_samples([feature_vector])[0] )
        # update histogram
        h_score_samples.observe(response["anomaly_score"])
    
    end = time.time()
    # update latency histogram
    h_latency.observe(end - start)

    return response


