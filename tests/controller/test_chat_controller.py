import pytest
from flask import Flask


class TestChatController:
    def setup_method(self):
        self.app = Flask(__name__)
        self.app.app_context().push()

        with self.app.app_context():
            from llm_writer_workshop.controller.chat_controller import chat_bp

            self.app.register_blueprint(chat_bp)
            self.client = self.app.test_client()

    def test_submit_happy_path(self, mocker):
        data = {"text": "Hello"}
        expected_feedbacks = ["Hello, how can I assist you?"]
        mock_chat = mocker.patch("llm_writer_workshop.service.chat_service.chat")
        mock_chat.return_value = expected_feedbacks

        response = self.client.post("/api/v1/generate-reviews", json=data)

        assert response.status_code == 200
        assert response.json == expected_feedbacks
        mock_chat.assert_called_once_with("Hello")

    def test_submit_empty_json(self):
        data = {}

        response = self.client.post("/api/v1/generate-reviews", json=data)

        assert response.status_code == 400
        assert response.json == {"error_message": "Empty JSON"}

    def test_submit_happy_path(self, mocker):
        data = {"text": "Hello"}
        expected_feedbacks = ["Hello, how can I assist you?"]
        mock_chat = mocker.patch("llm_writer_workshop.service.chat_service.chat")
        mock_chat.return_value = expected_feedbacks

        response = self.client.post("/api/v1/generate-reviews", json=data)

        assert response.status_code == 200
        assert response.json == expected_feedbacks
        mock_chat.assert_called_once_with("Hello")

    def test_submit_with_service_exception(self, mocker):
        data = {"text": "Hello"}
        mock_chat = mocker.patch("llm_writer_workshop.service.chat_service.chat")
        mock_chat.side_effect = Exception("Service error")

        response = self.client.post("/api/v1/generate-reviews", json=data)

        assert response.status_code == 500
        assert response.json == {"error_message": "An server error has occurred"}
        mock_chat.assert_called_once_with("Hello")


if __name__ == "__main__":
    pytest.main()
