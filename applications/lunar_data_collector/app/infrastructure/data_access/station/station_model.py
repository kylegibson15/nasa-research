from typing import List, Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

from app.infrastructure.data_access.sample.sample_model import SampleModel

class StationModel(SQLModel, table=True):
    __tablename__ = "stations"

    id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)
    name: str = Field(unique=True)
    mission_id: UUID = Field(default=None, foreign_key="missions.id")
     
#     samples: List[Optional["SampleModel"]] = Relationship(
#           back_populates="mission", 
#           cascade_delete=True,
#           sa_relationship_kwargs={"lazy": "selectin"}
#      )