from core.entities.document import Document
from infrastructure.data_access.mapper import Mapper
from infrastructure.data_access.document.document_model import DocumentModel

class DocumentMapper(Mapper[str, Document, DocumentModel]):    
    @staticmethod
    def entity_to_model(entity: Document) -> DocumentModel:
        return DocumentModel(
            id=entity.id,
            title=entity.title,
            summary=entity.summary,
            link=entity.link,
            author=entity.author,
            # updated=entity.updated,
            # published=entity.published,
            arxiv_id=entity.arxiv_id,
            mission_id=entity.mission_id
        )
    
    @staticmethod
    def model_to_entity(model: DocumentModel) -> Document:
        return Document(
            id=str(model.id),
            title=model.title,
            summary=model.summary,
            link=model.link,
            author=model.author,
            # updated=model.updated,
            # published=model.published,
            arxiv_id=model.arxiv_id,
            mission_id=str(model.mission_id)
        )
