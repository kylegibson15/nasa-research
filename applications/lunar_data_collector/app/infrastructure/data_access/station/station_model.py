from typing import List, Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

from app.infrastructure.data_access.sample.sample_model import SampleModel

class StationModel(SQLModel, table=True):
    __tablename__ = "stations"

    id: str = Field(primary_key=True, unique=True)
    name: str = Field(nullable=False)
     
    samples: List[Optional["SampleModel"]] = Relationship(
          back_populates="mission", 
          cascade_delete=True,
          sa_relationship_kwargs={"lazy": "selectin"}
     )