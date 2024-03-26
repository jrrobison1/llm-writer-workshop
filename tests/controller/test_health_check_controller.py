import unittest
from unittest.mock import patch
from flask import Flask
from llm_multi_model_workshop.controller.health_check_controller import health_bp


class TestHealthController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(health_bp)
        self.client = self.app.test_client()

    @patch(
        "llm_multi_model_workshop.controller.health_check_controller.health_check_service"
    )
    def test_health(self, mock_health_service):
        mock_health_service.health_check.return_value = "", 200

        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "")

        mock_health_service.health_check.assert_called_once()


if __name__ == "__main__":
    unittest.main()
