from typing import Optional
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.data_access.sample_display.sample_display_model import SampleDisplayModel

class SampleDisplayRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_sample_display_by_id(self, sample_display_id: str) -> Optional[SampleDisplayModel]:
        return await self.session.get(SampleDisplayModel, sample_display_id)

    async def create_sample_display(self, sample_display: SampleDisplayModel) -> SampleDisplayModel:
        self.session.add(sample_display)
        await self.session.commit()
        await self.session.refresh(sample_display)
        return sample_display