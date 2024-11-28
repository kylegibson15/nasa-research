from typing import Any
import boto3

class MessageProducer:
    def __init__(self, queue_url: str):
        self.queue_url = queue_url
        print(f"\nQUEUE URL: {self.queue_url}\n")
        self.sqs_client = boto3.client('sqs', endpoint_url=self.queue_url)

    def send_message(self, message_body: Any):
        print(f"\nSENDING MESSAGE: {message_body}\n")
        response = self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody="Hello, NASA"
        )

        print(response['MessageId'])