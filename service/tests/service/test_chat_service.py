from pytest import fixture
from llm_writer_workshop.service.chat_service import ChatService


@fixture
def mock_chatter_factory(mocker):
    return mocker.MagicMock()


@fixture
def chat_service(mock_chatter_factory):
    return ChatService(mock_chatter_factory)


def test_chat_success(chat_service, mock_chatter_factory, mocker):
    mock_chatter_factory.get_chatter.return_value.chat.return_value = "Review"
    assert chat_service.chatter_factory == mock_chatter_factory

    actual = chat_service.chat("text", "role", "model")

    assert actual == {
        "review": mock_chatter_factory.get_chatter.return_value.chat.return_value,
        "role": "role",
    }

    mock_chatter_factory.get_chatter.assert_called_once_with("role", "model")


def test_chat_exception(chat_service, mock_chatter_factory, mocker):
    error_message = (
        "I'm sorry, I'm having trouble processing your request. Please try again later."
    )

    mock_chatter_factory.get_chatter.return_value.chat.side_effect = Exception("Error")

    result = chat_service.chat("test_text", "test_role", "test_model")

    assert result == error_message
