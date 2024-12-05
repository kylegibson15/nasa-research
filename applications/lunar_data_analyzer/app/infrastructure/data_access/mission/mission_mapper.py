from core.entities.mission import Mission
from infrastructure.data_access.mapper import Mapper
from infrastructure.data_access.mission.mission_model import MissionModel

class MissionMapper(Mapper[str, Mission, MissionModel]):
    @staticmethod
    def response_to_entity(mission_name: str) -> Mission:
        return Mission(
            name=mission_name,
            samples=list(),
            stations=list(),
            landmarks=list(),
            documents=list(),
            analytics=None
        )
    
    @staticmethod
    def entity_to_model(entity: Mission) -> MissionModel:
        return MissionModel(
            id=entity.id,
            name=entity.name,
        )
    
    @staticmethod
    def model_to_entity(model: MissionModel) -> Mission:
        return Mission(
            id=str(model.id),
            name=model.name,
            samples=list(),
            stations=list(),
            landmarks=list(),
            documents=list(),
            analytics=None
        )
