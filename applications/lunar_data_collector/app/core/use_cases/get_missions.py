from app.core.entities.mission import Mission
from app.infrastructure.data_access.mission.mission_repository import MissionRepository

class GetMissionsUseCase:
    def __init__(self, mission_repository: MissionRepository):
        self.mission_repository = mission_repository

    async def execute(self) -> list[Mission]:
        return await self.mission_repository.get_missions()