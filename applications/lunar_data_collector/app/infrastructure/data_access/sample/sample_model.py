from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

class SampleModel(SQLModel, table=True):
     __tablename__ = "samples"

     id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
     original_sample_id: str | None = Field()
     generic_id: str | None = Field()
     bag_number: str | None = Field()
     original_weight: float | None = Field()
     sample_type: str | None = Field()
     sample_subtype: str | None = Field()
     pristinity: float | None = Field()
     pristinity_date: str | None = Field()
     has_thin_section: bool | None = Field()
     has_display: bool | None = Field()
     generic_description: str | None = Field()
     
     mission_id: UUID = Field(default=None, foreign_key="missions.id")
     # station_id: str | None = Field(default=None, foreign_key="stations.id")
     # landmark_id: str | None = Field(default=None, foreign_key="landmarks.id")
     # display_id: str | None = Field(default=None, foreign_key="sample_displays.id")
     # thin_section_id: str | None = Field(default=None, foreign_key="sample_thin_sections.id")

     # mission: "MissionModel" = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )

     # station: Optional["StationModel"] = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )

     # landmark: Optional["LandmarkModel"] = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )

     # display: Optional["SampleDisplayModel"] = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )

     # thin_section: Optional["SampleThinSectionModel"] = Relationship(
     #     back_populates="samples",
     #     sa_relationship_kwargs={"lazy": "selectin"}
     # )
