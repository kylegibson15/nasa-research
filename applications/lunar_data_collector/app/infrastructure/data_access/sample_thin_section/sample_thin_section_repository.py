from typing import Optional
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.data_access.sample_thin_section.sample_thin_section_model import SampleThinSectionModel

class SampleThinSectionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_sample_thin_section_by_id(self, sample_thin_section_id: str) -> Optional[SampleThinSectionModel]:
        return await self.session.get(SampleThinSectionModel, sample_thin_section_id)

    async def create_sample_thin_section(self, sample_thin_section: SampleThinSectionModel) -> SampleThinSectionModel:
        self.session.add(sample_thin_section)
        await self.session.commit()
        await self.session.refresh(sample_thin_section)
        return sample_thin_section