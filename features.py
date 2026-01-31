import json
import time
import boto3

SSM_PARAM = "/fastapi/prod/features"
REFRESH_SECONDS = 30

_client = boto3.client("ssm", region_name="us-east-1")
_cache = {"data": {}, "ts": 0}


def get_features():
    now = time.time()
    if now - _cache["ts"] > REFRESH_SECONDS:
        resp = _client.get_parameter(
            Name=SSM_PARAM,
            WithDecryption=False,
        )
        _cache["data"] = json.loads(resp["Parameter"]["Value"])
        _cache["ts"] = now

    return _cache["data"]
