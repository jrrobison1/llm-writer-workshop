import pytest
from flask import Flask
from llm_writer_workshop.controller.health_check_controller import health_bp


class TestHealthController:
    def setup_method(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(health_bp)
        self.client = self.app.test_client()

    def test_health(self, mocker):
        mock_health_check_service = mocker.patch(
            "llm_writer_workshop.controller.health_check_controller.health_check_service"
        )
        mock_health_check_service.health_check.return_value = "", 200

        response = self.client.get("/health")
        assert response.status_code == 200
        assert response.data.decode() == ""

        mock_health_check_service.health_check.assert_called_once()


if __name__ == "__main__":
    pytest.main()
