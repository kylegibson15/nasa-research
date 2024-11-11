import logging
from sqlmodel import UUID, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.entities.station import Station
from app.infrastructure.data_access.station.station_mapper import StationMapper
from app.infrastructure.data_access.station.station_model import StationModel

class StationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_station_by_id(self, station_id: UUID) -> Station | None :
        try:
            statement = select(StationModel).where(StationModel.id == station_id)
            response = await self.session.exec(statement)
            station = response.first()
            return StationMapper.model_to_entity(station) if station else None
        except Exception as e:
            raise Exception(f"Error while getting station by id - Error: {e}")
        
    async def get_station_by_name(self, station_name: str) -> Station | None :
        try:
            statement = select(StationModel).where(StationModel.name == station_name)
            response = await self.session.exec(statement)
            station = response.first()
            return StationMapper.model_to_entity(station) if station else None
        except Exception as e:
            raise Exception(f"Error while getting station by name - Error: {e}")
        
    async def get_stations_by_mission_id(self, mission_id: UUID) -> list[Station | None]:
        try:
            statement = select(StationModel).where(StationModel.mission_id == mission_id)
            response = await self.session.exec(statement)
            results = response.all()
            return [StationMapper.model_to_entity(model) for model in results]
        except Exception as e:
            raise Exception(f"Error while getting station by mission id - Error: {e}")

    async def get_stations(self) -> list[Station | None]:
        try:
            statement = select(StationModel)
            results = await self.session.exec(statement)           
            return [StationMapper.model_to_entity(model) for model in results]
        except Exception as e:
            raise Exception(f"Failed getting stations: {e}") from e
        
    async def create_station(self, entity: Station) -> Station:
        try:
            model = StationMapper.entity_to_model(entity)
            self.session.add(model)
            await self.session.commit()
            await self.session.refresh(model)
            return StationMapper.model_to_entity(model)
        except Exception as e:
            logging.error(f"Error creating mission: {e}")
            return None