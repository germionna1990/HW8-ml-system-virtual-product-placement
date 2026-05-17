from fastapi import FastAPI
from prometheus_client import Histogram, generate_latest
from fastapi.responses import Response
import time
import random

app = FastAPI()

LATENCY = Histogram(
    "request_latency_seconds",
    "Request latency in seconds"
)

@app.get("/predict")
def predict():
    start = time.time()

    time.sleep(random.uniform(0.1, 0.5))

    LATENCY.observe(time.time() - start)

    return {"prediction": "movie_recommendation"}

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )