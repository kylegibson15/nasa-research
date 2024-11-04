from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

from app.infrastructure.data_access.sample.sample_model import SampleModel

class SampleDisplayModel(SQLModel, table=True):
    __tablename__ = "sample_displays"

    id: str = Field(primary_key=True, unique=True)
    display_id: str = Field(nullable=False)
    region: str = Field(nullable=False)
    display_url: str = Field(nullable=False)
    display_location: str = Field(nullable=False)
    address_line_1: str = Field(nullable=False)
    address_line_2: str = Field(nullable=True)
    address_line_3: str = Field(nullable=True)
    phone: str = Field(nullable=False)
    latitude: str = Field(nullable=False)
    longitude: str = Field(nullable=False)
    city: str = Field(nullable=False)
    state: str = Field(nullable=False)
    country: str = Field(nullable=False)
    country_id: str = Field(nullable=False)
    zoom_level: int = Field()
    description: str = Field(nullable=False)
    generic: float = Field()
    speicific: float = Field()
     
    sample: Optional["SampleModel"] = Relationship(
          back_populates="display", 
          cascade_delete=True,
          sa_relationship_kwargs={"lazy": "selectin"}
     )