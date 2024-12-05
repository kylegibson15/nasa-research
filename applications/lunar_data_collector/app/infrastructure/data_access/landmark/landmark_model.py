from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel

class LandmarkModel(SQLModel, table=True):
     __tablename__ = "landmarks"

     id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
     name: str = Field(unique=True)
     mission_id: UUID = Field(default=None, foreign_key="missions.id")
