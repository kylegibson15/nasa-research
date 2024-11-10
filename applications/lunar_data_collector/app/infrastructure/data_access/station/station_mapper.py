from app.core.entities.station import Station
from app.infrastructure.data_access.mapper import Mapper
from app.infrastructure.data_access.station.station_model import StationModel

class StationMapper(Mapper[str, Station, StationModel]):
    @staticmethod
    def response_to_entity(station_name: str) -> Station:
        print(f"\STATION RESPONSE TO ENTITY: {station_name}\n")
        return Station(
            name=station_name,
            # samples=list(),
            mission_id=None,
            mission=None
        )
    
    @staticmethod
    def entity_to_model(entity: Station) -> StationModel:
        print(f"\STATION ENTITY TO MODEL: {entity}\n")
        return StationModel(
            id=entity.id,
            name=entity.name,
            mission_id=entity.mission_id
        )
    
    @staticmethod
    def model_to_entity(model: StationModel) -> Station:
        print(f"\STATION MODEL TO ENTITY: {model}\n")
        return Station(
            id=model.id,
            name=model.name,
            # samples=list()
            mission=None,
            mission_id=model.mission_id
        )
