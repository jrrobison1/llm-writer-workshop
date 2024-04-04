import pytest
from unittest.mock import MagicMock
from llm_writer_workshop.service.chat_service import ChatService
from llm_writer_workshop.service.config_service import ConfigService


@pytest.fixture
def config_service_mock():
    mock = MagicMock(spec=ConfigService)
    mock.get_writer_prompt.return_value = "Writer prompt"
    mock.get_writer_name.return_value = "Writer"
    mock.get_editor_prompt.return_value = "Editor prompt"
    mock.get_editor_name.return_value = "Editor"
    mock.get_agent_prompt.return_value = "Agent prompt"
    mock.get_agent_name.return_value = "Agent"
    mock.get_publisher_prompt.return_value = "Publisher prompt"
    mock.get_publisher_name.return_value = "Publisher"
    return mock


@pytest.fixture
def chat_service(config_service_mock):
    return ChatService(config_service_mock)


def test_init(chat_service, config_service_mock, mocker):
    assert chat_service.config_service == config_service_mock

    config_service_mock.get_writer_prompt.assert_called_once()
    config_service_mock.get_writer_name.assert_called_once()
    config_service_mock.get_editor_prompt.assert_called_once()
    config_service_mock.get_editor_name.assert_called_once()
    config_service_mock.get_agent_prompt.assert_called_once()
    config_service_mock.get_agent_name.assert_called_once()
    config_service_mock.get_publisher_prompt.assert_called_once()
    config_service_mock.get_publisher_name.assert_called_once()

    # Check that the chatter objects were created with the correct parameters. Don't
    # check the properties of the chatter objects. Test the parameters that
    # the chatter objects were created with in the __init__ method


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
