from uuid import UUID
from core.entities.analytics import Analytics
from infrastructure.data_access.analytics.analytics_repository import AnalyticsRepository
from infrastructure.data_access.document.document_repository import DocumentRepository
from infrastructure.document_api_client.document_api_client import DocumentApiClient
from infrastructure.data_access.mission.mission_repository import MissionRepository

class ProcessMessageUseCase:
    def __init__(
            self, 
            mission_repository: MissionRepository, 
            document_repository: DocumentRepository, 
            analytics_repository: AnalyticsRepository, 
            document_api_client: DocumentApiClient
        ):
        self.mission_repository = mission_repository
        self.document_repository = document_repository
        self.analytics_repository = analytics_repository
        self.document_api_client = document_api_client

    async def execute(self, mission_name: str):
        print(f"Received mission_name: {mission_name}")
        
        mission = await self.mission_repository.get_mission_by_name(mission_name)

        if not mission:
            raise Exception(f"Mission {mission_name} does not exist.")
        
        related_document = self.document_api_client.get(mission.name)

        for document in related_document:
            document.mission_id = mission.id
            print(f"\nAttempting to create document: {document}")
            await self.document_repository.create_document(document)

        samples_count = len(mission.samples)
        stations_count = len(mission.stations)
        landmarks_count = len(mission.landmarks)

        documents = await self.document_repository.get_documents_by_mission_id(mission.id)
        
        analytics = Analytics(
            mission_id=mission.id,
            samples_count=samples_count,
            stations_count=stations_count,
            landmarks_count=landmarks_count,
            documents_count=len(documents)
        )
        
        await self.analytics_repository.create_analytics(analytics)
