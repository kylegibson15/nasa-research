import boto3

if __name__ == "__main__":
  sqs_client = boto3.client(
    "sqs",
    endpoint_url="http://sqs.us-east-1.localhost.localstack.cloud:4566",
    region_name="us-east-1", 
    aws_access_key_id="", 
    aws_secret_access_key="", 
  )

  try:
    response = sqs_client.create_queue(QueueName="analyze")
    print(f"Queue created successfully: {response['QueueUrl']}")
  except Exception as error:
    print(f"Error creating queue: {error}")