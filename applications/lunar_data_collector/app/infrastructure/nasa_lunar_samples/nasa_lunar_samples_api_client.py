import logging
from typing import TypeVar
import requests
from app.infrastructure.nasa_lunar_samples.nasa_lunar_samples_responses import LandmarkApiResponse, MissionApiResponse, SampleApiResponse, SampleClassificationApiResponse, SampleDisplayApiResponse, SampleThinSectionApiResponse, StationApiResponse
from app.infrastructure.settings import Settings

T = TypeVar('T')

class NasaLunarSamplesApiClient():
    
    def __init__(self, settings: Settings):
        logging.info("initializing NasaLunarSamplesApiClient.")
        self.base_url = settings.nasa_lunar_samples_url
        # Multiple Samples
        self.samples_by_mission_path = lambda mission: f"samplesbymission/{mission}"
        self.samples_by_classification_path = lambda sample_type: f"samplesbyclassification/{sample_type}"
        self.samples_by_subtype_path = lambda sample_type, sample_subtype: f"samplesbysubtype/{sample_type}?subtype={sample_subtype}"
        self.samples_by_station_path = lambda mission, station: f"samplesbystation/{mission}/{station}"
        self.samples_by_landmark_path = lambda mission, landmark: f"samplesbylandmark/{mission}/{landmark}"
        # Individual Sample Data
        self.sample_details_path = lambda generic_id: f"sampledetails/{generic_id}"
        self.sample_thin_sections_path = lambda generic_id: f"samplethinsections/{generic_id}"
        self.sample_displays_path = lambda generic_id: f"sampledisplays/{generic_id}"
        # List APIs
        self.list_missions_path = "listmissions"
        self.list_sample_classification_path = "listsampleclassification"
        self.list_station_by_mission_path = lambda mission: f"liststationsbymission/{mission}"
        self.list_landmarks_by_mission_path = lambda mission: f"listlandmarksbymission/{mission}"
        
        logging.info("NasaLunarSamplesApiClient successfully initialized.")

    # Multiple Samples APIs
    def samples_by_mission(self, mission: str) -> list[SampleApiResponse]:
        return self._get(f"{self.base_url}/{self.samples_by_mission_path(mission)}")

    def samples_by_classification(self, sample_type: str) -> list[SampleApiResponse]:
        return self._get(f"{self.base_url}/{self.samples_by_classification_path(sample_type)}")
    
    def samples_by_subtype(self, sample_type: str, sample_subtype: str) -> list[SampleApiResponse]:
        return self._get(f"{self.base_url}/{self.samples_by_subtype_path(sample_type, sample_subtype)}")

    def samples_by_station(self, mission: str, station: str) -> list[SampleApiResponse]:
        return self._get(f"{self.base_url}/{self.samples_by_station_path(mission, station)}")

    def samples_by_landmark(self, mission: str, landmark: str) -> list[SampleApiResponse]:
        return self._get(f"{self.base_url}/{self.samples_by_landmark_path(mission, landmark)}")

    # Individual Sample Data APIs
    def sample_details(self, generic_id: str) -> list[SampleApiResponse]:
        return self._get(f"{self.base_url}/{self.sample_details_path(generic_id)}")

    def sample_thin_sections(self, generic_id: str) -> list[SampleThinSectionApiResponse]:
        return self._get(f"{self.base_url}/{self.sample_thin_sections_path(generic_id)}")

    def sample_displays(self, generic_id: str) -> list[SampleDisplayApiResponse]:
        return self._get(f"{self.base_url}/{self.sample_displays_path(generic_id)}")

    # List APIs
    def list_missions(self) -> set[str | None]:
        data: list[MissionApiResponse] = self._get(f"{self.base_url}/{self.list_missions_path}")
        return set([mission["MISSION"] for mission in data])
    
    def list_sample_classification(self) -> list[tuple[str, str | None]]:
        data: list[SampleClassificationApiResponse] = self._get(f"{self.base_url}/{self.list_sample_classification_path}")
        return [(classification["SAMPLETYPE"], classification["SAMPLESUBTYPE"]) for classification in data]

    def list_station_by_mission(self, mission: str) -> set[str | None]:
        data: list[StationApiResponse] = self._get(f"{self.base_url}/{self.list_station_by_mission_path(mission)}")
        return set([station["STATION"] for station in data])

    def list_landmarks_by_mission(self, mission: str) -> set[str | None]:
        data: list[LandmarkApiResponse] = self._get(f"{self.base_url}/{self.list_landmarks_by_mission_path(mission)}")
        return set([landmark["LANDMARK"] for landmark in data])
    
    def _get(self, url: str) -> list[T]:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    