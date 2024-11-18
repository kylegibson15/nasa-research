from uuid import UUID
from app.core.entities.mission import Mission
from app.infrastructure.data_access.mission.mission_repository import MissionRepository
from app.infrastructure.data_access.sample.sample_repository import SampleRepository
from app.infrastructure.data_access.station.station_repository import StationRepository

class GetMissionByIdUseCase:
    def __init__(
            self, 
            mission_repository: MissionRepository,
            sample_repository: SampleRepository,
            station_repository: StationRepository
        ):
        self.mission_repository = mission_repository
        self.sample_repository = sample_repository
        self.station_repository = station_repository

    async def execute(self, mission_id: UUID | str) -> Mission:
        mission = await self.mission_repository.get_mission_by_id(mission_id)
        mission.samples = await self.sample_repository.get_samples_by_mission_id(mission.id)
        mission.stations = await self.station_repository.get_stations_by_mission_id(mission.id)

        return mission