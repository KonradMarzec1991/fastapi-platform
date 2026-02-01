import os
import uuid

from fastapi import FastAPI
from fastapi import HTTPException

from features import get_features
from heavy_work import now, do_heavy_work
from sqs_client import enqueue_task

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
    request_id = str(uuid.uuid4())
    received_at = now()

    print(f"[{received_at}] REQUEST received request_id={request_id}")

    features = get_features()

    # ===== DEGRADED MODE =====
    if not features.get("slow_endpoint"):
        enqueue_task({
            "request_id": request_id,
            "received_at": received_at
        })

        print(f"[{now()}] QUEUED request_id={request_id}")

        return {
            "status": "queued",
            "request_id": request_id,
            "received_at": received_at
        }

    # ===== NORMAL MODE =====
    result = do_heavy_work(
        request_id=request_id,
        received_at=received_at
    )

    return {
        "status": "processed",
        **result
    }

@app.get("/_features")
def features():
    return get_features()

@app.get("/new-api")
def new_api():
    if not get_features().get("new_api"):
        raise HTTPException(status_code=404)

    return {"msg": "new api enabled"}
