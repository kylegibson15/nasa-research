from app.core.entities.document import Document
from app.infrastructure.data_access.document.document_repository import DocumentRepository


class GetDocumentsUseCase:
    def __init__(self, documents_repository: DocumentRepository):
        self.documents_repository = documents_repository

    async def execute(self) -> list[Document]:
        return await self.documents_repository.get_documents()