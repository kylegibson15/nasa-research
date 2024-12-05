from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel

class DocumentModel(SQLModel, table=True):
    __tablename__ = "documents"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str | None = Field(index=True)  # Add index for performance
    summary: str | None = Field()
    link: str | None = Field(unique=True)
    author: str | None = Field()
    # updated: datetime | None = Field()
    # published: datetime | None = Field()
    arxiv_id: str | None = Field(unique=True)
    mission_id: UUID = Field(default=None, foreign_key="missions.id")

    __table_args__ = (
        UniqueConstraint("title", "mission_id", name="unique_document_per_mission"),
    )
