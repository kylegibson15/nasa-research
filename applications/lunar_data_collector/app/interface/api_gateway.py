from abc import ABC, abstractmethod

class ApiGateway(ABC):
    @abstractmethod
    async def fetch_mission_data(self, mission_id: str) -> list[dict]:
        pass