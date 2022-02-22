import pandas as pd
import numpy as np
import requests
import random

# URL of the web service used for prediction
SERVICE_URL = "http://localhost:8000/prediction"
  
def get_prediction(feature_vector):
    # set the value for score based on a a random number
    score = random.randrange(100) < 25
    # make prediction request
    r = requests.post(SERVICE_URL, json = { 
          "feature_vector": feature_vector.tolist(),
          "score": score
          } 
        )
    # print(r) # useful for return codes
    print(r.text)


def test_predictions():
    # load test data
    test_df = pd.read_csv("test.csv")
    
    # get prediction for first data row only    
    # print(test_df.loc[1, :].values)
    # get_prediction(test_df.loc[1, :].values)
    
    # get predictions for each row (feature vector) of the test data
    test_df.apply(get_prediction, axis = 1)
    # get model information
    r = requests.get("http://localhost:8000/model_information")
    print(r.text)


if __name__ == '__main__':
    test_predictions()




