import boto3
import os

REGION = os.getenv("AWS_REGION", "us-east-1")

_ssm = boto3.client("ssm", region_name=REGION)


def set_param(name: str, value: str):
    _ssm.put_parameter(
        Name=name,
        Value=value,
        Type="String",
        Overwrite=True,
    )
