from uuid import uuid4
from app.core.entities.sample import Sample
from app.infrastructure.data_access.mapper import Mapper
from app.infrastructure.data_access.sample.sample_model import SampleModel
from app.infrastructure.nasa_lunar_samples.nasa_lunar_samples_responses import SampleApiResponse

class SampleMapper(Mapper[SampleApiResponse, Sample, SampleModel]):
    @staticmethod
    def response_to_entity(sample_raw: SampleApiResponse) -> Sample:
        print(f"\nSAMPLE RESPONSE TO ENTITY:\n\t{sample_raw}\n")
        return Sample(
            id=str(uuid4()),
            sample_id=str(sample_raw["SAMPLEID"]) or "",
            generic_id=sample_raw["GENERIC"] or "",
            bag_number=sample_raw["BAGNUMBER"] or "",
            original_weight=sample_raw["ORIGINALWEIGHT"] or 0.0,
            sample_type=sample_raw["SAMPLETYPE"] or "",
            sample_subtype=sample_raw["SAMPLESUBTYPE"] or "",
            pristinity=sample_raw["PRISTINITY"] or 0.0,
            pristinity_date=sample_raw["PRISTINITYDATE"] or "",
            has_thin_section=sample_raw["HASTHINSECTION"] or False,
            has_display_sample=sample_raw["HASDISPLAYSAMPLE"] or False,
            generic_description=sample_raw["GENERICDESCRIPTION"] or ""
        )

    @staticmethod
    def entity_to_model(entity: Sample) -> SampleModel:
        print(f"\nSAMPLE ENTITY TO MODEL\n\t{entity}\n")
        return SampleModel(
            id=entity.id,
            sample_id=entity.sample_id,
            generic_id=entity.generic_id,
            bag_number=entity.bag_number,
            original_weight=entity.original_weight,
            sample_type=entity.sample_type,
            sample_subtype=entity.sample_subtype,
            pristinity=entity.pristinity,
            pristinity_date=entity.pristinity_date,
            has_thin_section=entity.has_thin_section,
            has_display=entity.has_display_sample,
            generic_description=entity.generic_description
        )

    @staticmethod
    def model_to_entity(model: SampleModel) -> Sample:
        print(f"\nSAMPLE MODEL TO ENTITY\n\t{model}\n")
        return Sample(
            id=model.id,
            sample_id=model.sample_id,
            generic_id=model.generic_id,
            bag_number=model.bag_number,
            original_weight=model.original_weight,
            sample_type=model.sample_type,
            sample_subtype=model.sample_subtype,
            pristinity=model.pristinity,
            pristinity_date=model.pristinity_date,
            has_thin_section=model.has_thin_section,
            has_display_sample=model.has_display,
            generic_description=model.generic_description
        )
