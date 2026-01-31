import os
import time

from fastapi import FastAPI
from fastapi import HTTPException

from features import get_features

APP_ENV = os.getenv("APP_ENV", "dev")
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "PIPELINE FINAL TEST",
    }

@app.get("/version")
def version():
    return {"version": os.getenv("APP_VERSION", "unknown")}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/env")
def env():
    return {
        "env": APP_ENV,
        "log_level": LOG_LEVEL
    }

@app.get("/load")
def load():
    x = 0
    for i in range(10_000_000):
        x += i
    return {"status": "ok"}


@app.get("/slow")
def slow_endpoint():
    features = get_features()

    if not features.get("slow_endpoint", False):
        raise HTTPException(status_code=404, detail="Feature disabled")

    import time
    time.sleep(2)

    return {"msg": "slow endpoint active"}

@app.get("/_features")
def features():
    return get_features()

@app.get("/new-api")
def new_api():
    if not get_features().get("new_api"):
        raise HTTPException(status_code=404)

    return {"msg": "new api enabled"}
