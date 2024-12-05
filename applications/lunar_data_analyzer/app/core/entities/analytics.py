from dataclasses import dataclass

@dataclass
class Analytics:
    mission_id: str
    samples_count: int = 0
    stations_count: int = 0
    landmarks_count: int = 0
    documents_count: int = 0
    id: str | None = None
    