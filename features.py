import json
import os
import time
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SSM_PARAM = os.getenv("FEATURE_FLAGS_PARAM", "")
REFRESH_SECONDS = int(os.getenv("FEATURE_FLAGS_TTL", "30"))
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

_client = boto3.client("ssm", region_name=AWS_REGION)

_cache = {
    "data": {},
    "ts": 0,
}

def get_features() -> dict:
    try:
        if not SSM_PARAM:
            logger.warning("FEATURE_FLAGS_PARAM not set")
            return {}

        now = time.time()
        if now - _cache["ts"] < REFRESH_SECONDS:
            return _cache["data"]

        resp = _client.get_parameter(
            Name=SSM_PARAM,
            WithDecryption=False,
        )

        features = json.loads(resp["Parameter"]["Value"])
        _cache["data"] = features
        _cache["ts"] = now

        logger.info("Feature flags refreshed: %s", features)
        return features

    except Exception as e:
        logger.exception("FEATURE FLAGS ERROR")
        return {}
