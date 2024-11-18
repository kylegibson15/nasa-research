from app.core.entities.mission import Mission
from app.infrastructure.data_access.mission.mission_repository import MissionRepository
            

class GetMissionNamesUseCase:
    def __init__(
            self, 
            mission_repository: MissionRepository,
        ):
        self.mission_repository = mission_repository

    async def execute(self) -> list[Mission]:
        missions = await self.mission_repository.get_mission_names_and_ids()
        return [{"label": label, "id": id} for id, label in missions]
    