import logging
from app.interface.api_gateway import ApiGateway

class FetchTechPortMissionDataUseCase:
    def __init__(self, api_gateway: ApiGateway):
        self.api_gateway = api_gateway
        logging.info("fetch mission data use case successfully initialized")

    async def execute(self, mission_id: str) -> list[dict]:
        logging.info(f"execute - mission_id: {mission_id}")
        data = await self.api_gateway.fetch_mission_data(mission_id)
        logging.info("\n------------------\n")
        logging.info(data)
        logging.info("\n------------------\n")
        return data