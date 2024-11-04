from typing import Optional
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.data_access.station.station_model import StationModel

class StationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_station_by_id(self, station_id: str) -> Optional[StationModel]:
        return await self.session.get(StationModel, station_id)

    async def create_station(self, station: StationModel) -> StationModel:
        self.session.add(station)
        await self.session.commit()
        await self.session.refresh(station)
        return station