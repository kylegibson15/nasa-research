import logging
from app.core.entities.landmark import Landmark
from app.infrastructure.data_access.landmark.landmark_mapper import LandmarkMapper
from sqlalchemy import UUID, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.data_access.landmark.landmark_model import LandmarkModel

class LandmarkRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_landmark_by_id(self, landmark_id: UUID) -> LandmarkModel | None:
        try:
            statement = select(LandmarkModel).where(LandmarkModel.id == landmark_id)
            response = await self.session.exec(statement)
            landmark = response.first()
            return LandmarkMapper.model_to_entity(landmark) if landmark else None
        except Exception as e:
            raise Exception(f"Error while getting landmark by id - Error: {e}")
        
    
    async def get_landmark_by_name(self, landmark_name: str) -> LandmarkModel | None:
        try:
            statement = select(LandmarkModel).where(LandmarkModel.name == landmark_name)
            response = await self.session.exec(statement)
            landmark = response.first()
            return LandmarkMapper.model_to_entity(landmark) if landmark else None
        except Exception as e:
            raise Exception(f"Error while getting landmark by name - Error: {e}")

    async def create_landmark(self, entity: Landmark) -> LandmarkModel:
        try:
            model = LandmarkMapper.entity_to_model(entity)
            self.session.add(model)
            await self.session.commit()
            await self.session.refresh(model)
            return LandmarkMapper.model_to_entity(model)
        except Exception as e:
            logging.error(f"Error creating mission: {e}")
            return None