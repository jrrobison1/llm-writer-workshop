import pytest
from unittest.mock import MagicMock, Mock, patch
from llm_writer_workshop.service import config_service
from llm_writer_workshop.chatter.mistral_chatter import MistralChatter
from llm_writer_workshop.chatter.openai_chatter import OpenAIChatter
from llm_writer_workshop.service import chat_service


@pytest.fixture(autouse=True)
def mock_config_service(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("llm_writer_workshop.service.config_service", mock)
    return mock


@pytest.fixture(autouse=True)
def mock_chatters(monkeypatch):
    monkeypatch.setattr(chat_service, "editor_chatter", MagicMock(spec=MistralChatter))
    monkeypatch.setattr(chat_service, "agent_chatter", MagicMock(spec=OpenAIChatter))
    monkeypatch.setattr(chat_service, "writer_chatter", MagicMock(spec=OpenAIChatter))
    monkeypatch.setattr(
        chat_service, "publisher_chatter", MagicMock(spec=OpenAIChatter)
    )


def test_chat_success():
    chat_service.editor_chatter.chat.return_value = "Editor feedback"
    chat_service.agent_chatter.chat.return_value = "Agent feedback"
    chat_service.writer_chatter.chat.return_value = "Writer feedback"
    chat_service.publisher_chatter.chat.return_value = "Publisher feedback"

    text = "Sample text for testing"
    result = chat_service.chat(text)

    chat_service.editor_chatter.chat.assert_called_once()
    chat_service.agent_chatter.chat.assert_called_once()
    chat_service.writer_chatter.chat.assert_called_once()
    chat_service.publisher_chatter.chat.assert_called_once()

    assert len(result) == 4
    assert chat_service.chat("Hello") == [
        {"text": "Editor feedback", "model": "GPT-4", "role": "editor"},
        {"text": "Agent feedback", "model": "GPT-4", "role": "agent"},
        {"text": "Writer feedback", "model": "GPT-4", "role": "writer"},
        {"text": "Publisher feedback", "model": "GPT-4", "role": "publisher"},
    ]


def test_chat_exception():
    chat_service.editor_chatter.chat.side_effect = Exception("Mocked exception")

    result = chat_service.chat("Hello")

    assert (
        result
        == "I'm sorry, I'm having trouble processing your request. Please try again later."
    )

    chat_service.editor_chatter.chat.assert_called_once()


if __name__ == "__main__":
    pytest.main()
