from abc import ABC, abstractmethod

from core.entities.document import Document


class DocumentApiClient(ABC):
    @abstractmethod
    def get(self, query_value: str) -> list[Document] | None:
        pass