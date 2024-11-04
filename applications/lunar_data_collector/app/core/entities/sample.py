from dataclasses import dataclass
from typing import Any

@dataclass
class Sample:
    id: str
    sample_id: str
    generic_id: str
    bag_number: str
    original_weight: float
    sample_type: str
    sample_subtype: str
    pristinity: float
    pristinity_date: str
    has_thin_section: bool
    has_display_sample: bool
    generic_description: str
    # mission_id: str | None
    # mission: Any | None
    