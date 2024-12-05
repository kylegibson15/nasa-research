from app.core.entities.mission import Mission
from app.infrastructure.data_access.analytics.analytics_repository import AnalyticsRepository
from app.infrastructure.data_access.document.document_repository import DocumentRepository
from app.infrastructure.data_access.landmark.landmark_repository import LandmarkRepository
from app.infrastructure.data_access.mission.mission_repository import MissionRepository
from app.infrastructure.data_access.sample.sample_repository import SampleRepository
from app.infrastructure.data_access.station.station_repository import StationRepository

class GetMissionsUseCase:
    def __init__(
            self, 
            mission_repository: MissionRepository,
            sample_repository: SampleRepository,
            station_repository: StationRepository,
            landmarks_repository: LandmarkRepository,
            documents_repository: DocumentRepository,
            analytics_repository: AnalyticsRepository,
        ):
        self.mission_repository = mission_repository
        self.sample_repository = sample_repository
        self.station_repository = station_repository
        self.landmarks_repository = landmarks_repository
        self.documents_repository = documents_repository
        self.analytics_repository = analytics_repository

    async def execute(self) -> list[Mission]:
        missions = await self.mission_repository.get_missions()

        for mission in missions:
            mission.samples = await self.sample_repository.get_samples_by_mission_id(mission.id)
            mission.stations = await self.station_repository.get_stations_by_mission_id(mission.id)
            mission.landmarks = await self.landmarks_repository.get_landmarks_by_mission_id(mission.id)
            mission.documents = await self.documents_repository.get_documents_by_mission_id(mission.id)
            mission.analytics = await self.analytics_repository.get_analytics_by_mission_id(mission.id)

        return missions