import os

from fastapi import FastAPI

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
