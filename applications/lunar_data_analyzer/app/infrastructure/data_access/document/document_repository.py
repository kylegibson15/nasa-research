from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from core.entities.document import Document
from infrastructure.data_access.document.document_mapper import DocumentMapper
from infrastructure.data_access.document.document_model import DocumentModel

class DocumentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_documents_by_mission_id(self, mission_id: UUID) -> list[Document]:
        try:
            statement = select(DocumentModel).where(DocumentModel.mission_id == mission_id)
            response = await self.session.exec(statement)
            documents = response.all()
            return [DocumentMapper.model_to_entity(document) for document in documents]
        except Exception as e:
            raise Exception(f"Error while getting document by mission id {mission_id} - Error: {e}")

    async def get_document_by_mission_id_and_title(self, mission_id: UUID, title: str) -> Document:
        try:
            statement = select(DocumentModel).where(DocumentModel.mission_id == mission_id).where(DocumentModel.title == title)
            response = await self.session.exec(statement)
            document = response.one_or_none()
            return DocumentMapper.model_to_entity(document)
        except Exception as e:
            raise Exception(f"Error while getting document by mission id {mission_id} - Error: {e}")
        
    async def create_document(self, document: Document) -> Document:
        try:
            existing_document = self.get_document_by_mission_id_and_title(document.mission_id, document.title)
            if existing_document is None:
                model = DocumentMapper.entity_to_model(document)
                self.session.add(model)
                await self.session.commit()
                await self.session.refresh(model)
                print(f"\nSUCCESSFULLY CREATED DOCUMENT: {model}\n")
                return DocumentMapper.model_to_entity(model)
            else:
                return existing_document
        except Exception as e:
            raise Exception(f"Failed creating document: {e}") from e
            