import boto3

class SQSMessageConsumer:
    def __init__(self, queue_url: str):
        self.queue_url = queue_url
        self.sqs_client = boto3.client('sqs', endpoint_url=self.queue_url)


    def start(self, message_handler: callable):
        while True:
            response = self.sqs_client.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10
            )

            print(f"CONSUMER MESSAGE RESPONSE: {response}")

            if 'Messages' in response:
                for message in response['Messages']:
                    print(f"\nTHIS ONE HAS A MESSAGE :: {message}\n")
                    receipt_handle = message['ReceiptHandle']
                    message_body = message['Body']

                    message_handler(message_body)

                    self.sqs_client.delete_message(
                        QueueUrl=self.queue_url,
                        ReceiptHandle=receipt_handle
                    )