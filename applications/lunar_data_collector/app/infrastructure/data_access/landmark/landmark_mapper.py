from app.core.entities.landmark import Landmark
from app.infrastructure.data_access.mapper import Mapper
from app.infrastructure.data_access.landmark.landmark_model import LandmarkModel

class LandmarkMapper(Mapper[str, Landmark, LandmarkModel]):
    @staticmethod
    def response_to_entity(landmark_name: str) -> Landmark:
        return Landmark(
            name=landmark_name,
            # samples=list(),
            mission_id=None,
            mission=None
        )
    
    @staticmethod
    def entity_to_model(entity: Landmark) -> LandmarkModel:
        return LandmarkModel(
            id=entity.id,
            name=entity.name,
            mission_id=entity.mission_id
        )
    
    @staticmethod
    def model_to_entity(model: LandmarkModel) -> Landmark:
        return Landmark(
            id=model.id,
            name=model.name,
            # samples=list()
            mission=None,
            mission_id=model.mission_id
        )
