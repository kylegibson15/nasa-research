from app.core.entities.station import Station
from app.infrastructure.data_access.station.station_repository import StationRepository

class GetStationsUseCase:
    def __init__(self, stations_repository: StationRepository):
        self.stations_repository = stations_repository

    async def execute(self) -> list[Station]:
        return await self.stations_repository.get_stations()
    