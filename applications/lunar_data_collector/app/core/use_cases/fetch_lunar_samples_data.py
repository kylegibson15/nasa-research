import logging

from app.infrastructure.data_access.mission.mission_mapper import MissionMapper
from app.infrastructure.data_access.mission.mission_repository import MissionRepository
from app.infrastructure.data_access.sample.sample_mapper import SampleMapper
from app.infrastructure.data_access.sample.sample_repository import SampleRepository
from app.infrastructure.nasa_lunar_samples.nasa_lunar_samples_api_client import NasaLunarSamplesApiClient

class FetchLunarSamplesDataUseCase:
    def __init__(
            self, 
            api_client: NasaLunarSamplesApiClient, 
            mission_repository: MissionRepository, 
            sample_repository: SampleRepository
        ):
        self.api_client = api_client
        self.mission_repository = mission_repository
        self.sample_repository = sample_repository
        logging.info("fetch lunar samples data use case successfully initialized")

    async def execute(self) -> list[dict]:
        missions_response = await self.api_client.list_missions()
        # sample_classifications = await self.api_client.list_sample_classification()
        print(f"missions response: {missions_response}")
        for mission_name in missions_response:
            mission = MissionMapper.response_to_entity(mission_name)
            mission_model = await self.mission_repository.create_mission(MissionMapper.entity_to_model(mission))
            print(f"mission_model: {mission_model}")
            
            samples_by_mission = await self.api_client.samples_by_mission(mission.name)
            for sample_response in samples_by_mission:
                sample = SampleMapper.response_to_entity(sample_response)

                sample_model = await self.sample_repository.create_sample(SampleMapper.entity_to_model(sample))
                print(f"sample_model: {sample_model}")
                # sample_model.mission = mission_model
                # mission_model.samples.append(sample_model)

            # stations = await self.api_client.list_station_by_mission(mission)
            # print(f"\n\tall stations: {stations}")

            # for station in stations:
            #     print(f"\n\tstation: {station}")
            #     samples_by_station = await self.api_client.samples_by_station(mission, station)
            #     print(f"\n\t\tsamples by station: {samples_by_station}")
            
            # landmarks = await self.api_client.list_landmarks_by_mission(mission)
            # print(f"\n\tall landmarks: {landmarks}")

            # for landmark in landmarks:
            #     print(f"\n\tlandmark: {landmark}")
            #     samples_by_landmark = await self.api_client.samples_by_landmark(mission, landmark)
            #     print(f"\n\t\tsamples_by_landmark: {samples_by_landmark}")

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
        return {"Status": "Ok"}
