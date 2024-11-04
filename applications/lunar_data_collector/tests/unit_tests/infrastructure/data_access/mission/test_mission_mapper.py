import unittest
from uuid import uuid4

from app.core.entities.mission import Mission
from app.infrastructure.data_access.mission.mission_mapper import MissionMapper
from app.infrastructure.data_access.mission.mission_model import MissionModel

class TestMissionMapper(unittest.TestCase):

    def test_response_to_entity(self):
        mission_name = "Test Mission"
        mission_entity = MissionMapper.response_to_entity(mission_name)

        self.assertIsInstance(mission_entity, Mission)
        self.assertIsNotNone(mission_entity.id)
        self.assertEqual(mission_entity.name, mission_name)

    def test_entity_to_model(self):
        mission_id = str(uuid4())
        mission_name = "Another Test Mission"
        mission_entity = Mission(id=mission_id, name=mission_name)

        mission_model = MissionMapper.entity_to_model(mission_entity)

        self.assertIsInstance(mission_model, MissionModel)
        self.assertEqual(mission_model.id, mission_id)
        self.assertEqual(mission_model.name, mission_name)

    def test_model_to_entity(self):
        mission_id = str(uuid4())
        mission_name = "Third Test Mission"
        mission_model = MissionModel(id=mission_id, name=mission_name)

        mission_entity = MissionMapper.model_to_entity(mission_model)

        self.assertIsInstance(mission_entity, Mission)
        self.assertEqual(mission_entity.id, mission_id)
        self.assertEqual(mission_entity.name, mission_name)
