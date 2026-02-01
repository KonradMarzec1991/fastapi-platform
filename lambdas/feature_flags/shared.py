import json

from common.ssm import set_param

FEATURE_PARAM = "/fastapi/prod/features"


def set_feature(enabled: bool):
    set_param(FEATURE_PARAM, json.dumps({"new_api": True, "slow_endpoint": enabled}))