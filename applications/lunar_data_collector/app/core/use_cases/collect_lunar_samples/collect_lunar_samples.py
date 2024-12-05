import dataclasses
import json
import logging

from app.core.entities.mission import Mission
from app.core.entities.sample import Sample
from app.core.entities.station import Station
from app.core.use_cases.collect_lunar_samples.collect_lunar_samples_response import CollectLunarSamplesResponse
from app.infrastructure.data_access.mission.mission_mapper import MissionMapper
from app.infrastructure.data_access.mission.mission_repository import MissionRepository
from app.infrastructure.data_access.sample.sample_mapper import SampleMapper
from app.infrastructure.data_access.sample.sample_repository import SampleRepository
from app.infrastructure.data_access.station.station_mapper import StationMapper
from app.infrastructure.data_access.station.station_repository import StationRepository
from app.infrastructure.nasa_lunar_samples.nasa_lunar_samples_api_client import NasaLunarSamplesApiClient
from app.infrastructure.data_access.landmark.landmark_mapper import LandmarkMapper
from app.infrastructure.data_access.landmark.landmark_repository import LandmarkRepository
from app.infrastructure.event_messaging.message_producer import MessageProducer

class CollectLunarSamplesUseCase:
    def __init__(
            self, 
            api_client: NasaLunarSamplesApiClient,
            mission_repository: MissionRepository, 
            sample_repository: SampleRepository,
            station_repository: StationRepository,
            landmark_repository: LandmarkRepository,
            message_producer: MessageProducer
        ):
        self.api_client = api_client
        self.mission_repository = mission_repository
        self.sample_repository = sample_repository
        self.station_repository = station_repository
        self.landmark_repository = landmark_repository
        self.message_producer = message_producer
        logging.info("fetch lunar samples data use case successfully initialized")
    

    async def execute(self, limit: int = 2) -> CollectLunarSamplesResponse:
        all_missions = list()
        missions_api_response = self.api_client.list_missions()
        # sample_classifications = await self.api_client.list_sample_classification()
        logging.debug(f"missions response: {missions_api_response}")

        unique_sample_type = set()

        for mission_name in missions_api_response:
            mission = await self._get_mission(mission_name)
            samples = await self._get_samples_by_mission(mission)
            stations = await self._get_stations_by_mission(mission)
            landmarks = await self._get_landmarks_by_mission(mission)

            mission.samples = samples
            mission.stations = stations
            mission.landmarks = landmarks

            for sample in samples:
                unique_sample_type.add(sample.sample_type)
            
            logging.info(mission)
            all_missions.append(mission)
            
            self.message_producer.send_message(mission.name)
       
        # unique_ids = set()
        # for (sample_type, sample_subtype) in sample_classifications:
        #     print(f"sample type: {sample_type} & sample subtype: {sample_subtype}")
        #     samp_class = await self.api_client.samples_by_classification(sample_type)
        #     print(f"\n\tsample by class: {samp_class}")

        #     samp_sub = await self.api_client.samples_by_subtype(sample_type, sample_subtype)
        #     print(f"\n\tsample by subtype: {samp_sub}")

        #     for sample in samp_class:
        #         generic_id = sample["GENERIC"]
        #         unique_ids.add(generic_id)
                
        # print(f"\nunique generic ids: {unique_ids} - count: {len(unique_ids)}")

        # for generic_id in unique_ids:
        #     sample_details = await self.api_client.sample_details(generic_id)
        #     print(f"\n\t\tsample details: {sample_details}")
                
        #     sample_thin_section = await self.api_client.sample_thin_sections(generic_id)
        #     print(f"\nsample thin section:\n\t{sample_thin_section}")

        #     sample_displays = await self.api_client.sample_displays(generic_id)
        #     print(f"\n\t\tsample display: {sample_displays}")
        return CollectLunarSamplesResponse(missions=all_missions[:limit], total_count=len(all_missions), page_size=limit)

    async def _get_mission(self, mission_name: str) -> Mission:
        mission_entity = MissionMapper.response_to_entity(mission_name)
        mission = await self.mission_repository.get_mission_by_name(mission_entity.name)
        print(f"\nMISSION: {mission}\n")
        if mission is None:
            mission = await self.mission_repository.create_mission(mission_entity)
            
        return mission
    

    async def _get_samples_by_mission(self, mission: Mission) -> list[Sample]:
        samples_by_mission = self.api_client.samples_by_mission(mission.name)
        samples = list()
        for sample_response in samples_by_mission:
            entity = SampleMapper.response_to_entity(sample_response)
            entity.mission_id = mission.id

            sample = await self.sample_repository.get_sample_by_unique_properties(entity)

            if sample is None:
                sample = await self.sample_repository.create_sample(entity)

            samples.append(sample)
        
        return samples
    
    # async def _get_samples_by_mission_and_station(self, mission: Mission, station: Station) -> list[Sample]:
    #     samples_by_station = await self.api_client.samples_by_station(mission.name, station.name)
    #     samples = list()
        
    #     print(f"\n\t\tsamples by station: {samples_by_station}")
    #     samples.append(station)

    #     return samples
    
    async def _get_stations_by_mission(self, mission: Mission) -> list[Station]:
        stations_by_mission = self.api_client.list_station_by_mission(mission.name)
        stations = list()
        for station_name in stations_by_mission:
            if station_name is None:
                continue

            entity = StationMapper.response_to_entity(station_name)
            entity.mission_id = mission.id

            station = await self.station_repository.get_station_by_name(entity.name)

            if station is None:
                station = await self.station_repository.create_station(entity)

            # samples_by_station = await self.api_client.samples_by_station(mission.name, station_name)
            # print(f"\n\t\tsamples by station: {samples_by_station}")
            stations.append(station)

        return stations
    
    async def _get_landmarks_by_mission(self, mission: Mission) -> list[str]:
        landmarks_by_mission = self.api_client.list_landmarks_by_mission(mission)
        landmarks = list()

        for landmark_name in landmarks_by_mission:
            if landmark_name is None:
                continue

            entity = LandmarkMapper.response_to_entity(landmark_name)
            entity.mission_id = mission.id

            landmark = await self.landmark_repository.get_landmark_by_name(entity.name)

            if landmark is None:
                landmark = await self.landmark_repository.create_landmark(entity)

            # samples_by_landmark = await self.api_client.samples_by_landmark(mission, landmark)
            # print(f"\n\t\tsamples_by_landmark: {samples_by_landmark}")
            landmarks.append(landmark)

            print(f"\n\tlandmark: {landmark}")
            