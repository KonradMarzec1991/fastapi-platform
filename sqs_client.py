import boto3
import json
import os

sqs = boto3.client("sqs")
QUEUE_URL = os.environ["SLOW_QUEUE_URL"]

def enqueue_task(message: dict):
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )
