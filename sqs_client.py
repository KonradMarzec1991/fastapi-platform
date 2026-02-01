import boto3
import json
import os

QUEUE_URL = os.getenv("SLOW_QUEUE_URL", "https://sqs.us-east-1.amazonaws.com/622711946516/fastapi-slow-queue")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

sqs = boto3.client("sqs", region_name=AWS_REGION)


def enqueue_task(message: dict):
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )
