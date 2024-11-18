from fastapi.testclient import TestClient

from app.api.endpoints import app
from app.core.entities.mission import Mission

client = TestClient(app)

class TestEndpoints:

    def test_get_missions(self):
        response: list[Mission] = client.get("/missions")
        data = response.json()
        assert response.status_code == 200
        # assert len(data) >= 0
        # first_mission: Mission = data[0]
        # assert first_mission["name"] == "Luna 20"
        # samples = first_mission["samples"]
        # assert len(samples) > 0
