from typing import Optional
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.data_access.landmark.landmark_model import LandmarkModel

class LandmarkRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_landmark_by_id(self, landmark_id: str) -> Optional[LandmarkModel]:
        return await self.session.get(LandmarkModel, landmark_id)

    async def create_landmark(self, landmark: LandmarkModel) -> LandmarkModel:
        self.session.add(landmark)
        await self.session.commit()
        await self.session.refresh(landmark)
        return landmark