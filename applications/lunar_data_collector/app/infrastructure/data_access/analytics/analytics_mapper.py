from app.core.entities.analytics import Analytics
from app.infrastructure.data_access.mapper import Mapper
from app.infrastructure.data_access.analytics.analytics_model import AnalyticsModel

class AnalyticsMapper(Mapper[str, Analytics, AnalyticsModel]):    
    @staticmethod
    def entity_to_model(entity: Analytics) -> AnalyticsModel:
        return AnalyticsModel(
            id=entity.id,
            mission_id=entity.mission_id,
            samples_count=entity.samples_count,
            stations_count=entity.stations_count,
            landmarks_count=entity.landmarks_count
        )
    
    @staticmethod
    def model_to_entity(model: AnalyticsModel) -> Analytics:
        return Analytics(
            id=str(model.id),
            mission_id=model.mission_id,
            samples_count=model.samples_count,
            stations_count=model.stations_count,
            landmarks_count=model.landmarks_count
        )
