from fastapi.testclient import TestClient

from app.api.endpoints import app
from app.core.entities.mission import Mission

client = TestClient(app)

class TestEndpoints:

    def test_get_missions(self):
        response: list[Mission] = client.get("/missions")
        data = response.json()
        assert response.status_code == 200
        assert "missions" in data.keys()
        assert len(data["missions"]) > 0