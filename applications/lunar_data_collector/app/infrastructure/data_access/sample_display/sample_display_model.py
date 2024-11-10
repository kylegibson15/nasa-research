from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

from app.infrastructure.data_access.sample.sample_model import SampleModel

class SampleDisplayModel(SQLModel, table=True):
    __tablename__ = "sample_displays"

    id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
    display_id: str = Field() 
    region: str = Field()
    display_url: str = Field()
    display_location: str = Field()
    address_line_1: str = Field()
    address_line_2: str = Field()
    address_line_3: str = Field()
    phone: str = Field()
    latitude: str = Field()
    longitude: str = Field()
    city: str = Field()
    state: str = Field()
    country: str = Field()
    country_id: str = Field()
    zoom_level: int = Field()
    description: str = Field()
    generic: float = Field()
    speicific: float = Field()
     
#     sample: Optional["SampleModel"] = Relationship(
#           back_populates="display", 
#           cascade_delete=True,
#           sa_relationship_kwargs={"lazy": "selectin"}
#      )