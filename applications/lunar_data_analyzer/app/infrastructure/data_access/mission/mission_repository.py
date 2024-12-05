from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from core.entities.mission import Mission
from infrastructure.data_access.mission.mission_mapper import MissionMapper
from infrastructure.data_access.mission.mission_model import MissionModel

class MissionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_mission_by_name(self, mission_name: str) -> Mission | None:
        try:
            statement = select(MissionModel).where(MissionModel.name == mission_name)
            response = await self.session.exec(statement)
            mission = response.first()
            return MissionMapper.model_to_entity(mission) if mission is not None else None
        except Exception as e:
            raise Exception(f"Error while getting mission by name - name {mission_name} - Error: {e}")
