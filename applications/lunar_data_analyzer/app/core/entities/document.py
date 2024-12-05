from dataclasses import dataclass
from datetime import datetime

@dataclass
class Document:
    title: str
    summary: str
    link: str
    author: str | None
    # updated: datetime
    # published: datetime
    arxiv_id: str
    mission_id: str | None = None
    id: str | None = None