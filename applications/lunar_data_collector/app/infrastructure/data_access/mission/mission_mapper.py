from app.core.entities.mission import Mission
from app.infrastructure.data_access.mapper import Mapper
from app.infrastructure.data_access.mission.mission_model import MissionModel
# from app.infrastructure.data_access.sample.sample_mapper import SampleMapper

class MissionMapper(Mapper[str, Mission, MissionModel]):
    @staticmethod
    def response_to_entity(mission_name: str) -> Mission:
        return Mission(
            name=mission_name,
            samples=list(),
            stations=list()
        )
    
    @staticmethod
    def entity_to_model(entity: Mission) -> MissionModel:
        return MissionModel(
            id=entity.id,
            name=entity.name,
            # samples=[SampleMapper.entity_to_model(sample) for sample in entity.samples]
        )
    
    @staticmethod
    def model_to_entity(model: MissionModel) -> Mission:
        return Mission(
            id=model.id,
            name=model.name,
            samples=list(),
            stations=list()
            # samples=[SampleMapper.model_to_entity(sample) for sample in model.samples]
        )
