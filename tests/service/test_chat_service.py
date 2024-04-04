import pytest
from unittest.mock import MagicMock
from llm_writer_workshop.service.chat_service import ChatService
from llm_writer_workshop.service.config_service import ConfigService


@pytest.fixture
def config_service_mock():
    return MagicMock(spec=ConfigService)


@pytest.fixture
def chat_service(config_service_mock):
    return ChatService(config_service_mock)


def test_init(config_service_mock, mocker):
    chat_service = ChatService(config_service_mock)

    assert chat_service.config_service == config_service_mock
    assert chat_service.editor_chatter is not None
    assert chat_service.writer_chatter is not None
    assert chat_service.agent_chatter is not None
    assert chat_service.publisher_chatter is not None

    config_service_mock.get_writer_prompt.assert_called_once()
    config_service_mock.get_writer_name.assert_called_once()
    config_service_mock.get_editor_prompt.assert_called_once()
    config_service_mock.get_editor_name.assert_called_once()
    config_service_mock.get_agent_prompt.assert_called_once()
    config_service_mock.get_agent_name.assert_called_once()
    config_service_mock.get_publisher_prompt.assert_called_once()
    config_service_mock.get_publisher_name.assert_called_once()


def test_chat_success(chat_service, mocker):
    text = "Sample text for testing"
    editor_feedback = "Editor feedback"
    agent_feedback = "Agent feedback"
    writer_feedback = "Writer feedback"
    publisher_feedback = "Publisher feedback"

    mocker.patch.object(
        chat_service.editor_chatter, "chat", return_value=editor_feedback
    )
    mocker.patch.object(chat_service.agent_chatter, "chat", return_value=agent_feedback)
    mocker.patch.object(
        chat_service.writer_chatter, "chat", return_value=writer_feedback
    )
    mocker.patch.object(
        chat_service.publisher_chatter, "chat", return_value=publisher_feedback
    )

    result = chat_service.chat(text)

    assert len(result) == 4
    assert result[0]["text"] == editor_feedback
    assert result[1]["text"] == agent_feedback
    assert result[2]["text"] == writer_feedback
    assert result[3]["text"] == publisher_feedback


def test_chat_exception(chat_service, mocker):
    text = "Sample text for testing"
    error_message = (
        "I'm sorry, I'm having trouble processing your request. Please try again later."
    )

    mocker.patch.object(
        chat_service.editor_chatter, "chat", side_effect=Exception("Test exception")
    )

    result = chat_service.chat(text)

    assert result == error_message
