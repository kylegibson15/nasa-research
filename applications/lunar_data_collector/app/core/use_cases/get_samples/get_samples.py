from app.core.entities.sample import Sample
from app.core.use_cases.get_samples.get_samples_response import GetSamplesResponse
from app.infrastructure.data_access.sample.sample_repository import SampleRepository

class GetSamplesUseCase:
    def __init__(self, sample_repository: SampleRepository):
        self.sample_repository = sample_repository

    async def execute(self, page=1, limit=100) -> GetSamplesResponse:
        samples = await self.sample_repository.get_samples(limit)
        total_count = await self.sample_repository.get_samples_count()
        return GetSamplesResponse(total_count=total_count, page_size=limit, samples=samples[page-1:page*limit])
    