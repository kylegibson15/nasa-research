from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker

from app.core.use_cases.fetch_lunar_samples_data import FetchLunarSamplesDataUseCase
from app.core.use_cases.fetch_mission_data import FetchTechPortMissionDataUseCase
from app.core.use_cases.get_missions import GetMissionsUseCase
from app.infrastructure.data_access.mission.mission_repository import MissionRepository
from app.infrastructure.data_access.sample.sample_repository import SampleRepository
from app.infrastructure.nasa_lunar_samples.nasa_lunar_samples_api_client import NasaLunarSamplesApiClient
from app.infrastructure.nasa_tech_port_api_client import NasaTechPortApiClient
from app.infrastructure.settings import Settings

app = FastAPI()
settings = Settings()

engine = create_engine(
    url=settings.pg_dsn,
    echo=True,
    future=True,
    pool_size=20,
    pool_recycle=3600,
    max_overflow=20
)

async_engine = create_async_engine(
    url=settings.pg_async_dsn,
    echo=True,
    future=True,
    pool_size=20,
    pool_recycle=3600,
    max_overflow=20
)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, AsyncSession]:
    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@app.get("/")
def base():
    print(f"settings: {settings.model_dump()}")
    return {"Status": "Ok"}

@app.get("/init")
async def init():
    await init_db()
    return {"Status": "Ok"}

@app.get("/collect")
def collect_lunar_data():
    return {"Hello": "World"}

@app.get("/collect-lunar-samples-data")
async def collect_lunar_samples_data():
    async with get_async_session() as session:
        try:
            api_client = NasaLunarSamplesApiClient(settings)
            mission_repository = MissionRepository(session)
            sample_repository = SampleRepository(session)
            use_case = FetchLunarSamplesDataUseCase(api_client, mission_repository, sample_repository)
            response = await use_case.execute()
            logger.info(f"response: {response}")
            return response
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

@app.get("/missions")
async def get_missions():
    async with get_async_session() as session:
        try:
            mission_repository = MissionRepository(session)
            use_case = GetMissionsUseCase(mission_repository)
            response = await use_case.execute()
            print("\n\n----------\n\n")
            print(response)
            return response
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()

@app.get("/collect-mission-data")
async def collect_mission_data(mission_id: str):
    async with get_async_session() as session:
        try:
            if mission_id is None:
                raise ValueError(f"mission_id is required.")
            
            logger.info(f"mission_id: {mission_id}")
            api_client = NasaTechPortApiClient(settings)
            logger.info(f"api_client: {api_client}")
            use_case = FetchTechPortMissionDataUseCase(api_gateway=api_client)
            logger.info(f"use_case created")
            response = await use_case.execute(mission_id)
            logger.info(f"response received {response}")
            return response
        except Exception as e:
            logging.error(e)
        finally:
            await session.close()