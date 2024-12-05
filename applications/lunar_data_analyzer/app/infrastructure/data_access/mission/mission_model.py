from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

class MissionModel(SQLModel, table=True):
    __tablename__ = "missions"

    id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)
    name: str | None = Field(unique=True)
     
    # samples: list["SampleModel"] = Relationship( # type: ignore
    #       back_populates="mission",
    #     #   sa_relationship_kwargs={"lazy": "selectin"}
    #  )
