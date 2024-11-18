import logging
from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.entities.mission import Mission
from app.infrastructure.data_access.mission.mission_mapper import MissionMapper
from app.infrastructure.data_access.mission.mission_model import MissionModel

class MissionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_mission_by_id(self, mission_id: UUID) -> Mission | None:
        try:
            statement = select(MissionModel).where(MissionModel.id == mission_id)
            response = await self.session.exec(statement)
            mission = response.first()
            return MissionMapper.model_to_entity(mission) if mission else None
        except Exception as e:
            raise Exception(f"Error while getting mission by id - Error: {e}")
        
    async def get_mission_by_name(self, mission_name: str) -> Mission | None:
        try:
            statement = select(MissionModel).where(MissionModel.name == mission_name)
            response = await self.session.exec(statement)
            mission = response.first()
            return MissionMapper.model_to_entity(mission) if mission is not None else None
        except Exception as e:
            raise Exception(f"Error while getting mission by name - name {mission_name} - Error: {e}")

    async def get_missions(self) -> list[Mission | None]:
        try:
            statement = select(MissionModel)
            results = await self.session.exec(statement)           
            entities: list[Mission] = []
            for mission in results.all():
                entity = MissionMapper.model_to_entity(mission)
                entities.append(entity)
            return entities
        except Exception as e:
            raise Exception(f"Error while getting all missions: {e}")
        
    async def get_mission_names_and_ids(self) -> list[tuple[str, int]]:
        try:
            statement = select(MissionModel.id, MissionModel.name)
            results = await self.session.exec(statement)
            return results.all()
        except Exception as e:
            raise Exception(f"Error while getting mission names and IDs: {e}")

    async def create_mission(self, entity: Mission) -> Mission:
        try:
            model = MissionMapper.entity_to_model(entity)
            self.session.add(model)
            await self.session.commit()
            await self.session.refresh(model)
            return MissionMapper.model_to_entity(model)
        except Exception as e:
            logging.error(f"Error creating mission: {e}")
            return None