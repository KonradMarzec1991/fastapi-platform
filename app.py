import os

from fastapi import FastAPI

APP_VERSION = os.getenv("APP_VERSION", "dev")

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "PIPELINE FINAL TEST",
    }

@app.get("/version")
def version():
    return {"version": APP_VERSION}