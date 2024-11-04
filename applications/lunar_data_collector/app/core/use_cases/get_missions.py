from app.infrastructure.data_access.mission.mission_mapper import MissionMapper
from app.infrastructure.data_access.mission.mission_model import MissionModel
from app.infrastructure.data_access.mission.mission_repository import MissionRepository
from app.infrastructure.nasa_lunar_samples.nasa_lunar_samples_api_client import NasaLunarSamplesApiClient

class GetMissionsUseCase:
    def __init__(self, mission_repository: MissionRepository):
        self.mission_repository = mission_repository

    async def execute(self) -> list[MissionModel]:
        missions = await self.mission_repository.get_missions()
        print(f"\nMISSIONS\n\t{missions}\n")
        mission_entities = []
        for mission in missions:
            print(f"\nSINGLE MISSION: {mission}")
            if mission is not None:
                mission_entities.append(MissionMapper.model_to_entity(mission))
        return mission_entities