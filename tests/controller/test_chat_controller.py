import unittest
from unittest.mock import patch
from flask import Flask
from llm_multi_model_workshop.controller.chat_controller import chat_bp


class TestChatController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(chat_bp)
        self.client = self.app.test_client()

    @patch("llm_multi_model_workshop.service.chat_service.chat")
    def test_submit_happy_path(self, mock_chat):
        data = {"text": "Hello"}
        expected_feedbacks = ["Hello, how can I assist you?"]
        mock_chat.return_value = expected_feedbacks

        response = self.client.post("/chat/submit", json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"feedbacks": expected_feedbacks})
        mock_chat.assert_called_once_with("Hello")

    def test_submit_empty_json(self):
        data = {}

        response = self.client.post("/chat/submit", json=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error_message": "Empty JSON"})

    @patch("llm_multi_model_workshop.service.chat_service.chat")
    def test_submit_happy_path(self, mock_chat):
        data = {"text": "Hello"}
        expected_feedbacks = ["Hello, how can I assist you?"]
        mock_chat.return_value = expected_feedbacks

        response = self.client.post("/chat/submit", json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"feedbacks": expected_feedbacks})
        mock_chat.assert_called_once_with("Hello")

    @patch("llm_multi_model_workshop.service.chat_service.chat")
    def test_submit_with_service_exception(self, mock_chat):
        data = {"text": "Hello"}
        mock_chat.side_effect = Exception("Service error")

        response = self.client.post("/chat/submit", json=data)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            response.json, {"error_message": "An server error has occurred"}
        )
        mock_chat.assert_called_once_with("Hello")


if __name__ == "__main__":
    unittest.main()
