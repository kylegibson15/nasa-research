from dataclasses import dataclass
from typing import Any
from uuid import UUID

@dataclass
class Station:
    mission_id: str
    mission: Any | None
    name: str | None 
    id: UUID | str | None = None
    