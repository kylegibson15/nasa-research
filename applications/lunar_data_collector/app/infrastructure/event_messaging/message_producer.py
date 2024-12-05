import boto3

class MessageProducer:
    def __init__(self, queue_url: str):
        self.queue_url = queue_url
        self.sqs_client = boto3.client(
            'sqs', 
            endpoint_url=self.queue_url, 
            region_name="us-east-1", 
            aws_access_key_id="", 
            aws_secret_access_key=""
        )

    def send_message(self, message_body: str):
        response = self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message_body
        )

        print(f"\nMESSAGE RESPONSE: {response['MessageId']}\n")