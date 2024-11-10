from uuid import UUID, uuid4
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from app.infrastructure.data_access.sample.sample_model import SampleModel

class LandmarkModel(SQLModel, table=True):
     __tablename__ = "landmarks"

     id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
     name: str = Field(unique=True)
     
    #  samples: List[Optional["SampleModel"]] = Relationship(
    #      back_populates="landmark",
    #      sa_relationship_kwargs={"lazy": "selectin"}
    #  )
