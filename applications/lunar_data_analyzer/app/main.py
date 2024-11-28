import asyncio

from core.use_cases.process_message import ProcessMessageUseCase
from infrastructure.messaging.sqs_message_consumer import SQSMessageConsumer
from infrastructure.settings import Settings


settings = Settings()

async def main():
    sqs_consumer = SQSMessageConsumer(settings.queue_url)
    use_case = ProcessMessageUseCase()

    def message_handler(message):
        use_case.execute(message)

    sqs_consumer.start(message_handler)

if __name__ == "__main__":
    print("Nasa Data Analyzer Starting...")
    asyncio.run(main())