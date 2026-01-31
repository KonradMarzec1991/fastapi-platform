import os

from fastapi import FastAPI


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
