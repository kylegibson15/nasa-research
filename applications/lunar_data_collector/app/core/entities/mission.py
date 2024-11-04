from dataclasses import dataclass
from typing import Any, List

@dataclass
class Mission:
    id: str | None
    name: str
    # samples: List[Any] | None