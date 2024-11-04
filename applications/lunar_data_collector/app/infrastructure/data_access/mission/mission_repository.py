from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.data_access.mission.mission_mapper import MissionMapper
from app.infrastructure.data_access.mission.mission_model import MissionModel

class MissionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_mission_by_id(self, mission_id: str) -> Optional[MissionModel]:
        return await self.session.get(MissionModel, mission_id)

    async def get_missions(self, ) -> List[Optional[MissionModel]]:
        print("\nGET MISSIONS\n")
        statement = select(MissionModel)
        results = await self.session.execute(statement)           
        entities = []
        for result in results:
            model: MissionModel = result[0]
            print(f"\nMODEL: {model}")
            entity = MissionMapper.model_to_entity(model)
            # entity.samples = model.samples
            entities.append(entity)
        return entities

    async def create_mission(self, mission: MissionModel) -> MissionModel:
        self.session.add(mission)
        await self.session.commit()
        await self.session.refresh(mission)
        return mission