from uuid import UUID, uuid4
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from app.infrastructure.data_access.sample.sample_model import SampleModel

class LandmarkModel(SQLModel, table=True):
     __tablename__ = "landmarks"

     id: str = Field(primary_key=True, unique=True)
     name: str = Field(nullable=False)
     
     samples: List[Optional["SampleModel"]] = Relationship(
         back_populates="landmark", 
         cascade_delete=True,
         sa_relationship_kwargs={"lazy": "selectin"}
     )
