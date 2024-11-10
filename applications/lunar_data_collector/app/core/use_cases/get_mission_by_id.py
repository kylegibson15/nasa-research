from uuid import UUID
from app.core.entities.mission import Mission
from app.infrastructure.data_access.mission.mission_repository import MissionRepository

class GetMissionByIdUseCase:
    def __init__(self, mission_repository: MissionRepository):
        self.mission_repository = mission_repository

    async def execute(self, mission_id: UUID | str) -> Mission:
        return await self.mission_repository.get_mission_by_id(mission_id)