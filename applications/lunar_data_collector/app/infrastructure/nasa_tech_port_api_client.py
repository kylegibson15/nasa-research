import logging
import requests
from app.infrastructure.settings import Settings
from app.interface.api_gateway import ApiGateway

class NasaTechPortApiClient(ApiGateway):
    
    def __init__(self, settings: Settings):
        logging.info("initializing NasaTechPortApiClient.")
        self.base_url = settings.nasa_tech_port_url
        self.curator_url = "https://curator.jsc.nasa.gov/rest/lunarapi/samples"
        self.nasa_api_key = settings.nasa_api_key
        # Multiple Samples
        self.samples_by_mission_path = lambda mission: f"samplesbymission/{mission}"
        self.samples_by_classification = lambda sample_type: f"samplesbyclassification/{sample_type}"
        self.samples_by_subtype = lambda sample_type, sample_subtype: f"samplesbysubtype/{sample_type}?subtype={sample_subtype}"
        self.samples_by_station = lambda mission, station: f"samplesbystation/{mission}/{station}"
        self.samples_by_landmark = lambda mission, landmark: f"samplesbylandmark/{mission}/{landmark}"
        # Individual Sample Data
        self.sample_details = lambda generic_id: f"sampledetails/{generic_id}"
        self.sample_thin_sections = lambda generic_id: f"samplethinsections/{generic_id}"
        self.sample_displays = lambda generic_id: f"sampledisplays/{generic_id}"
        # List Functions
        self.list_missions_path = "listmissions"
        self.list_sample_classification_path = "listsampleclassification"
        self.list_station_by_mission = lambda mission: f"liststationsbymission/{mission}"
        self.list_landmarks_by_mission_path = lambda mission: f"listlandmarksbymission/{mission}"
        
        logging.info("NasaTechPortApiClient successfully initialized.")

    async def list_missions(self):
        url = f"{self.curator_url}/{self.list_missions_path}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info(f"list missions data: {data}")
        return data
    
    async def list_sample_classification(self):
        url = f"{self.curator_url}/{self.list_sample_classification_path}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info(f"list sample classification data: {data}")

    async def fetch_mission_data(self, mission_id: str) -> list[dict]:
        logging.info(f"NasaTechPortApiClient.fetch_mission_data called with mission_id: {mission_id}")
        await self.list_missions()
        await self.list_sample_classification()
        # url = f"{self.base_url}/{mission_id}?api_key={self.nasa_api_key}"
        url = f"{self.curator_url}/{self.list_landmarks_by_mission_path(mission=mission_id)}"
        response = requests.get(url)
        logging.info(f"status: {response.status_code}")
        data = None
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            print(f"Error: {response.json()}")
        logging.debug(f"response from nasa tech port:\n\t- {response}")
        response.raise_for_status()
        return data