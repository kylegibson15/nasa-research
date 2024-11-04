from typing import Optional
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.data_access.sample.sample_model import SampleModel

class SampleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_sample_by_id(self, sample_id: str) -> Optional[SampleModel]:
        return await self.session.get(SampleModel, sample_id)

    async def create_sample(self, sample: SampleModel) -> SampleModel:
        self.session.add(sample)
        await self.session.commit()
        await self.session.refresh(sample)
        return sample