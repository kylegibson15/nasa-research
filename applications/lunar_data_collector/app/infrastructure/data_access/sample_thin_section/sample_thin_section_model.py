from typing import List, Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

from app.infrastructure.data_access.sample.sample_model import SampleModel

class SampleThinSectionModel(SQLModel, table=True):
    __tablename__ = "sample_thin_sections"

    id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
    generic_id: str = Field()
    specific: str = Field()
    weight: float = Field()
    description: str = Field()
    availability: float = Field()
     
#     samples: List[Optional["SampleModel"]] = Relationship(
#           back_populates="thin_sections", 
#           cascade_delete=True,
#           sa_relationship_kwargs={"lazy": "selectin"}
#      )