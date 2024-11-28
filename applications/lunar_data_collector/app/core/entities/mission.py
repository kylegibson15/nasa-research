from dataclasses import dataclass
from typing import Any

@dataclass
class Mission:
    name: str
    samples: list[Any | None]
    stations: list[Any | None]
    landmarks: list[Any | None]
    id: str | None = None
    