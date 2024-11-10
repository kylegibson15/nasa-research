from dataclasses import dataclass
from app.core.entities.sample import Sample


@dataclass
class GetSamplesResponse:
    total_count: int
    page_size: int
    samples: list[Sample]