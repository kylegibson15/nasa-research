from dataclasses import dataclass
from typing import Any
from uuid import UUID

@dataclass
class Sample:
    original_sample_id: str
    generic_id: str
    bag_number: str
    original_weight: float
    sample_type: str
    sample_subtype: str
    pristinity: float
    pristinity_date: str
    has_thin_section: bool
    has_display: bool
    generic_description: str
    mission_id: str
    mission: Any | None
    id: UUID | str | None = None
    