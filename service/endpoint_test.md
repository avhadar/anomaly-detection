### Testing the model_information endpoint:

* no parameters required

	curl -X 'GET' \
	  'http://0.0.0.0:8000/model_information' \
	  -H 'accept: application/json'

returns

	{
	  "bootstrap": false,
	  "contamination": 0.001,
	  "max_features": 1,
	  "max_samples": "auto",
	  "n_estimators": 100,
	  "n_jobs": null,
	  "random_state": 16,
	  "verbose": 0,
	  "warm_start": false
	}


### Testing the model_information endpoint:

* with score parameter set to **true**, for outlier point

	curl -X 'POST' \
	  'http://0.0.0.0:8000/prediction' \
	  -H 'accept: application/json' \
	  -H 'Content-Type: application/json' \
	  -d '{
	  "feature_vector": [
	    60.0, 10.0
	  ],
	  "score": true
	}'

returns

	{
	  "is_inlier": -1,
	  "anomaly_score": -0.8628660479537293
	}


* without score parameter, for outlier point

	curl -X 'POST' \
	  'http://0.0.0.0:8000/prediction' \
	  -H 'accept: application/json' \
	  -H 'Content-Type: application/json' \
	  -d '{
	  "feature_vector": [
	    60.0, 10.0
	  ]
	}'

returns

	{
	  "is_inlier": -1,
	}


* with score parameter set to **false**, for outlier point

	curl -X 'POST' \
	  'http://0.0.0.0:8000/prediction' \
	  -H 'accept: application/json' \
	  -H 'Content-Type: application/json' \
	  -d '{
	  "feature_vector": [
	    60.0, 10.0
	  ],
	  "score": false
	}

returns

	{
	  "is_inlier": -1,
	}


* with score parameter set to **true**, for inlier point

	curl -X 'POST' \
	  'http://0.0.0.0:8000/prediction' \
	  -H 'accept: application/json' \
	  -H 'Content-Type: application/json' \
	  -d '{
	  "feature_vector": [
	    5.0, 5.0
	  ],
	  "score": true
	}

returns

	{
	  "is_inlier": 1,
	  "anomaly_score": -0.8329192136757835
	}
