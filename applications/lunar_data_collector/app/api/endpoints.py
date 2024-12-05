import logging
import time
from typing import Annotated
from uuid import UUID


from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from prometheus_client import Counter, Histogram, make_asgi_app
from functools import wraps

from app.core.use_cases.collect_lunar_samples.collect_lunar_samples import CollectLunarSamplesUseCase
# from app.core.use_cases.fetch_mission_data import FetchTechPortMissionDataUseCase
from app.core.use_cases.get_documents import GetDocumentsUseCase
from app.core.use_cases.get_mission_by_id import GetMissionByIdUseCase
from app.core.use_cases.get_mission_names import GetMissionNamesUseCase
from app.core.use_cases.get_missions import GetMissionsUseCase
from app.core.use_cases.get_samples.get_samples import GetSamplesUseCase
from app.core.use_cases.get_stations import GetStationsUseCase
from app.infrastructure.data_access.analytics.analytics_repository import AnalyticsRepository
from app.infrastructure.data_access.document.document_repository import DocumentRepository
from app.infrastructure.event_messaging.message_producer import MessageProducer
from app.infrastructure.data_access.mission.mission_repository import MissionRepository
from app.infrastructure.data_access.sample.sample_repository import SampleRepository
from app.infrastructure.data_access.station.station_repository import StationRepository
from app.infrastructure.data_access.landmark.landmark_repository import LandmarkRepository
from app.infrastructure.nasa_lunar_samples.nasa_lunar_samples_api_client import NasaLunarSamplesApiClient
# from app.infrastructure.nasa_tech_port_api_client import NasaTechPortApiClient
from app.infrastructure.settings import Settings

REQUEST_COUNT = Counter('request_count', 'Total number of requests')
REQUEST_TIME = Histogram('request_duration_seconds', 'Request duration in seconds')
ERROR_COUNT = Counter('error_count', 'Total number of errors')

def time_it(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            REQUEST_COUNT.inc()
            total_time = time.time() - start_time
            REQUEST_TIME.observe(total_time)
            return result
        except Exception as e:
            ERROR_COUNT.inc()
            raise e  # Re-raise the exception

    return wrapper

settings = Settings()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"]  # Allows all headers   

)

async_engine = create_async_engine(
    url=settings.pg_async_dsn,
    # echo=True,
    future=True,
    pool_size=20,
    pool_recycle=3600,
    max_overflow=20
)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.post("/init")
@time_it
async def init():
    await init_db()
    return {"Status": "Ok"}

@app.post("/collect-lunar-samples")
@time_it
async def collect_lunar_samples_data():
    async with AsyncSession(async_engine) as session:
        try:
            api_client = NasaLunarSamplesApiClient(settings)
            mission_repository = MissionRepository(session)
            sample_repository = SampleRepository(session)
            station_repository = StationRepository(session)
            landmark_repository = LandmarkRepository(session)
            message_producer = MessageProducer(settings.queue_url)
            use_case = CollectLunarSamplesUseCase(
                api_client, 
                mission_repository, 
                sample_repository,
                station_repository,
                landmark_repository,
                message_producer
            )
            return await use_case.execute()
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

@app.get("/mission/{mission_id}")
@time_it
async def get_mission_by_id(mission_id: Annotated[UUID | str, Path(title="The ID of the mission to get")],):
    async with AsyncSession(async_engine) as session:
        try:
            mission_repository = MissionRepository(session)
            sample_repository = SampleRepository(session)
            station_repository = StationRepository(session)
            landmarks_repository = LandmarkRepository(session)
            documents_repository = DocumentRepository(session)
            analytics_repository = AnalyticsRepository(session)
            use_case = GetMissionByIdUseCase(mission_repository, sample_repository, station_repository, landmarks_repository, documents_repository, analytics_repository)
            return await use_case.execute(mission_id)
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

@app.get("/missions")
@time_it
async def get_missions():
    async with AsyncSession(async_engine) as session:
        try:
            mission_repository = MissionRepository(session)
            sample_repository = SampleRepository(session)
            station_repository = StationRepository(session)
            landmarks_repository = LandmarkRepository(session)
            documents_repository = DocumentRepository(session)
            analytics_repository = AnalyticsRepository(session)
            use_case = GetMissionsUseCase(mission_repository, sample_repository, station_repository, landmarks_repository, documents_repository, analytics_repository)
            return await use_case.execute()
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

@app.get("/mission-names")
@time_it
async def get_mission_names():
    async with AsyncSession(async_engine) as session:
        try:
            mission_repository = MissionRepository(session)
            use_case = GetMissionNamesUseCase(mission_repository)
            return await use_case.execute()
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

@app.get("/samples")
@time_it
async def get_samples():
    async with AsyncSession(async_engine) as session:
        try:
            sample_repository = SampleRepository(session)
            use_case = GetSamplesUseCase(sample_repository)
            return await use_case.execute()
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

@app.get("/stations")
@time_it
async def get_stations():
    async with AsyncSession(async_engine) as session:
        try:
            station_repository = StationRepository(session)
            use_case = GetStationsUseCase(station_repository)
            return await use_case.execute()
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

@app.get("/documents")
@time_it
async def get_documents():
    async with AsyncSession(async_engine) as session:
        try:
            documents_repository = DocumentRepository(session)
            use_case = GetDocumentsUseCase(documents_repository)
            return await use_case.execute()
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

# @app.get("/collect-mission-data")
# async def collect_mission_data(mission_id: str):
#     async with get_async_session() as session:
#         try:
#             if mission_id is None:
#                 raise ValueError(f"mission_id is required.")
            
#             logger.info(f"mission_id: {mission_id}")
#             api_client = NasaTechPortApiClient(settings)
#             logger.info(f"api_client: {api_client}")
#             use_case = FetchTechPortMissionDataUseCase(api_gateway=api_client)
#             logger.info(f"use_case created")
#             response = await use_case.execute(mission_id)
#             logger.info(f"response received {response}")
#             return response
#         except Exception as e:
#             logging.error(e)
#         finally:
#             await session.close()