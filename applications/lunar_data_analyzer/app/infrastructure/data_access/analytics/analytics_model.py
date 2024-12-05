from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel

class AnalyticsModel(SQLModel, table=True):
    __tablename__ = "analyticss"

    id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)
    samples_count: int = Field(default=0)
    stations_count: int = Field(default=0)
    landmarks_count: int = Field(default=0)
    documents_count: int = Field(default=0)
    mission_id: UUID = Field(default=None, foreign_key="missions.id")
