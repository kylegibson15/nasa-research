import logging
from uuid import UUID
from sqlalchemy import func
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import col, select

from app.core.entities.sample import Sample
from app.infrastructure.data_access.sample.sample_mapper import SampleMapper
from app.infrastructure.data_access.sample.sample_model import SampleModel

class SampleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_sample_by_unique_properties(self, entity: Sample) -> Sample | None:
        try:
            statement = select(SampleModel)
            if entity.id:
                statement = statement.where(SampleModel.id == entity.id)
            if entity.original_sample_id:
                statement = statement.where(SampleModel.original_sample_id == entity.original_sample_id)
            if entity.generic_id:
                statement = statement.where(SampleModel.generic_id == entity.generic_id)

            model = await self.session.exec(statement)
            sample = model.first()
            return SampleMapper.model_to_entity(sample) if sample else None
        except Exception as e:
            raise Exception(f"Error while getting sample by properties - Error: {e}")

    async def get_sample_by_id(self, sample_id: UUID) -> Sample | None:
        try:
            statement = select(SampleModel).where(SampleModel.id == sample_id)
            model = await self.session.exec(statement)
            sample = model.first()
            return SampleMapper.model_to_entity(sample) if sample else None
        except Exception as e:
            raise Exception(f"Failed to get sample by id... {e}") from e
    
    async def get_sample_by_original_id(self, original_id: str) -> Sample | None:
        logging.debug(f"GET SMAPLE ORIGINAL ID: {original_id}")
        try:
            statement = select(SampleModel).where(SampleModel.original_sample_id == original_id)
            model = await self.session.exec(statement)
            sample = model.first()
            return SampleMapper.model_to_entity(sample) if sample else None
        except Exception as e:
            raise Exception(f"Failed to get sample by original id... {e}") from e
    
    async def get_samples(self, limit: int) -> list[Sample | None]:
        try:
            statement = select(SampleModel).limit(limit)
            results = await self.session.exec(statement)       
            return [SampleMapper.model_to_entity(model) for model in results]
        except Exception as e:
            raise Exception(f"Failed getting samples: {e}") from e
        
    async def get_samples_count(self):
        try:
            statement = select(func.count(col(SampleModel.id)))
            count = await self.session.exec(statement)
            return count.one()
        except Exception as e:
            raise Exception(f"Failed getting samples count: {e}") from e

    async def create_sample(self, sample: Sample) -> Sample:
        try:
            model = SampleMapper.entity_to_model(sample)
            self.session.add(model)
            await self.session.commit()
            await self.session.refresh(model)
            return SampleMapper.model_to_entity(model)
        except Exception as e:
            raise Exception(f"Failed creating sample: {e}") from e