from unittest.mock import Mock, patch
import pytest
from fastapi.testclient import TestClient

from app.api.endpoints import app
from app.core.entities.mission import Mission

class TestEndpoints:
    @pytest.fixture
    def client(self):
        with TestClient(app) as client:
            yield client
    
    @patch("app.infrastructure.data_access.document.document_repository.DocumentRepository.get_documents")
    def test_get_documents(self, get_documents: Mock, client):
        get_documents.return_value = [{
                    "title": "test", 
                    "summary": "test-summary", 
                    "link": "test-link", 
                    "author": "test-author", 
                    "arxiv_id": "test-arxiv_id", 
                    "mission_id": "test-mission_id"
                }]
        response: list[Mission] = client.get("/documents")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        first_document = data[0]
        assert first_document["title"] == "test"
        assert first_document["summary"] == "test-summary"
        assert first_document["title"] == "test"
        assert first_document["summary"] == "test-summary"
        assert first_document["link"] == "test-link"
        assert first_document["author"] == "test-author"
        assert first_document["arxiv_id"] == "test-arxiv_id"
        assert first_document["mission_id"] == "test-mission_id"
