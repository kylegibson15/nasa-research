from dataclasses import dataclass

from app.core.entities.mission import Mission


@dataclass
class CollectLunarSamplesResponse:
    total_count: int
    page_size: int
    missions: list[Mission]
    

    