import pytest
from unittest.mock import MagicMock, Mock, patch
from llm_writer_workshop.service import config_service
from llm_writer_workshop.chatter.mistral_chatter import MistralChatter
from llm_writer_workshop.chatter.openai_chatter import OpenAIChatter
from llm_writer_workshop.service import chat_service


@pytest.fixture(autouse=True)
def mock_config_service(monkeypatch):
    mock_config = MagicMock(spec=config_service)
    monkeypatch.setattr(chat_service, "config_service", mock_config)
    return mock_config


@pytest.fixture(autouse=True)
def mock_chatters(monkeypatch):
    monkeypatch.setattr(chat_service, "editor_chatter", MagicMock(spec=MistralChatter))
    monkeypatch.setattr(chat_service, "agent_chatter", MagicMock(spec=OpenAIChatter))
    monkeypatch.setattr(chat_service, "writer_chatter", MagicMock(spec=OpenAIChatter))
    monkeypatch.setattr(
        chat_service, "publisher_chatter", MagicMock(spec=OpenAIChatter)
    )


def test_chat_success():
    text = "Sample text for testing"
    result = chat_service.chat(text)
    print(result)

    assert len(result) == 4


def test_chat_exception():
    chat_service.editor_chatter.chat.side_effect = Exception("Mocked exception")

    result = chat_service.chat("Hello")

    assert (
        result
        == "I'm sorry, I'm having trouble processing your request. Please try again later."
    )

    # Assert that the mocked chatter method was called
    chat_service.editor_chatter.chat.assert_called_once()


if __name__ == "__main__":
    pytest.main()
