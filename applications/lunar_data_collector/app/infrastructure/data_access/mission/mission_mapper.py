from uuid import uuid4
from app.core.entities.mission import Mission
from app.infrastructure.data_access.mapper import Mapper
from app.infrastructure.data_access.mission.mission_model import MissionModel

class MissionMapper(Mapper[str, Mission, MissionModel]):
    @staticmethod
    def response_to_entity(mission_name: str) -> Mission:
        print(f"\nMISSION RESPONSE TO ENTITY: {mission_name}\n")
        return Mission(
            id=str(uuid4()),
            name=mission_name,
        )
    
    @staticmethod
    def entity_to_model(entity: Mission) -> MissionModel:
        print(f"\nMISSION ENTITY TO MODEL: {entity}\n")
        return MissionModel(
            id=entity.id,
            name=entity.name
        )
    
    @staticmethod
    def model_to_entity(model: MissionModel) -> Mission:
        print(f"\nMISSION MODEL TO ENTITY: {model}\n")
        return Mission(
            id=model.id,
            name=model.name
        )
