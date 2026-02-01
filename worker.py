import os
import json
import boto3
from heavy_work import do_heavy_work

sqs = boto3.client("sqs")
QUEUE_URL = os.environ["SLOW_QUEUE_URL"]

def run():
    while True:
        resp = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=5,
            WaitTimeSeconds=20
        )

        for msg in resp.get("Messages", []):
            body = json.loads(msg["Body"])

            do_heavy_work(
                request_id=body["request_id"],
                received_at=body["received_at"]
            )

            sqs.delete_message(
                QueueUrl=QUEUE_URL,
                ReceiptHandle=msg["ReceiptHandle"]
            )

if __name__ == "__main__":
    run()
