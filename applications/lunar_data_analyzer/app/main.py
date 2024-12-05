import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from core.use_cases.process_message import ProcessMessageUseCase
from infrastructure.messaging.sqs_message_consumer import SQSMessageConsumer
from infrastructure.data_access.mission.mission_repository import MissionRepository
from infrastructure.data_access.document.document_repository import DocumentRepository
from infrastructure.data_access.analytics.analytics_repository import AnalyticsRepository
from infrastructure.document_api_client.arxiv_api_client import ArxivApiClient
from infrastructure.settings import Settings


settings = Settings()


async_engine = create_async_engine(
    url=settings.pg_async_dsn,
    echo=True,
    future=True,
    pool_size=20,
    pool_recycle=3600,
    max_overflow=20
)

async def main():
    async with AsyncSession(async_engine) as session:
        sqs_consumer = SQSMessageConsumer(settings.queue_url)
        mission_repository = MissionRepository(session)
        document_repository = DocumentRepository(session)
        analytics_repository = AnalyticsRepository(session)
        document_api_client = ArxivApiClient()
        use_case = ProcessMessageUseCase(mission_repository,document_repository, analytics_repository, document_api_client)

        # sqs_consumer.create_queue()

        async def message_handler(message):
            await use_case.execute(message)

        await sqs_consumer.start(message_handler)

if __name__ == "__main__":
    print("NASA Data Analyzer Starting...")
    asyncio.run(main())