from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

class SampleModel(SQLModel, table=True):
     __tablename__ = "samples"

     id: str | None = Field(primary_key=True, unique=True)
     sample_id: str | None = Field(nullable=False)
     generic_id: str | None = Field(nullable=True)
     bag_number: str | None = Field(nullable=True)
     original_weight: float | None = Field(nullable=True)
     sample_type: str | None = Field(nullable=True)
     sample_subtype: str | None = Field(nullable=True)
     pristinity: float | None = Field(nullable=True)
     pristinity_date: str | None = Field(nullable=True)
     has_thin_section: bool | None = Field(nullable=True)
     has_display: bool | None = Field(nullable=True)
     generic_description: str | None = Field(nullable=True)

     mission_id: str | None = Field(default=None, foreign_key="missions.id")
     mission: Optional["MissionModel"] = Relationship(
         back_populates="samples",
         sa_relationship_kwargs={"lazy": "selectin"}
     )

     # station_id: str | None = Field(default=None, foreign_key="stations.id")
     # station: Optional["StationModel"] = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )

     # landmark_id: str | None = Field(default=None, foreign_key="landmarks.id")
     # landmark: Optional["LandmarkModel"] = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )

     # display_id: str | None = Field(default=None, foreign_key="sample_displays.id")
     # display: Optional["SampleDisplayModel"] = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )

     # thin_section_id: str | None = Field(default=None, foreign_key="sample_thin_sections.id")
     # thin_section: Optional["SampleThinSectionModel"] = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )
