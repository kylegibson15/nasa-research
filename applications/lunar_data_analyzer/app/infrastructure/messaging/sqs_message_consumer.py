import boto3

class SQSMessageConsumer:
    def __init__(self, queue_url: str):
        print(f"\n\nQUEUE URL: {queue_url}\n\n")
        self.queue_url = queue_url
        self.sqs_client = boto3.client(
            "sqs",
            endpoint_url="http://sqs.us-east-1.localhost.localstack.cloud:4566",
            region_name="us-east-1", 
            aws_access_key_id="", 
            aws_secret_access_key="", 
        )
    
    def create_queue(self):
        response = self.sqs_client.create_queue(QueueName="analyze")
        print(f"Queue created successfully: {response['QueueUrl']}")

    async def start(self, message_handler: callable):
        print("NASA Data Analyzer Started")
        self.create_queue()
        while True:
            response = self.sqs_client.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10
            )

            print(f"RESPONSE: {response}")


            if 'Messages' in response:
                for message in response['Messages']:
                    receipt_handle = message['ReceiptHandle']
                    message_body = message['Body']

                    await message_handler(message_body)

                    self.sqs_client.delete_message(
                        QueueUrl=self.queue_url,
                        ReceiptHandle=receipt_handle
                    )