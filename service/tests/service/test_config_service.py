from pytest import fixture
from llm_writer_workshop.service.config_service import ConfigService


@fixture
def config_service():
    return ConfigService()


@fixture
def mock_file_read(mocker):
    mocker.patch(
        "toml.load",
        return_value={
            "agent_config": {
                "name": "Test Agent",
                "persona": "Testing persona for agent",
            },
            "editor_config": {
                "name": "Test Editor",
                "persona": "Testing persona for editor",
            },
            "writer_config": {
                "name": "Test Writer",
                "persona": "Testing persona for writer",
            },
            "publisher_config": {
                "name": "Test Publisher",
                "persona": "Testing persona for publisher",
            },
        },
    )


def test_initialize_config_logs_data(mocker, config_service, mock_file_read):
    mock_logger_debug = mocker.patch(
        "llm_writer_workshop.service.config_service.logger.debug"
    )
    config_service.initialize_config()
    mock_logger_debug.assert_called()


def test_initialize_config_loads_data(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.data["agent_config"]["name"] == "Test Agent"
    assert config_service.data["agent_config"]["persona"] == "Testing persona for agent"

    assert config_service.data["editor_config"]["name"] == "Test Editor"
    assert (
        config_service.data["editor_config"]["persona"] == "Testing persona for editor"
    )

    assert config_service.data["writer_config"]["name"] == "Test Writer"
    assert (
        config_service.data["writer_config"]["persona"] == "Testing persona for writer"
    )

    assert config_service.data["publisher_config"]["name"] == "Test Publisher"
    assert (
        config_service.data["publisher_config"]["persona"]
        == "Testing persona for publisher"
    )


def test_get_agent_name_with_config(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.get_agent_name() == "Test Agent"


def test_get_agent_name_without_config(config_service):
    assert config_service.get_agent_name() == "Agent"


def test_get_agent_prompt_with_config(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.get_agent_prompt() == "Testing persona for agent"


def test_get_agent_prompt_without_config(config_service):
    assert config_service.get_agent_prompt() == "You are a creative writing agent"


def test_get_editor_name_with_config(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.get_editor_name() == "Test Editor"


def test_get_editor_name_without_config(config_service):
    assert config_service.get_editor_name() == "Editor"


def test_get_editor_prompt_with_config(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.get_editor_prompt() == "Testing persona for editor"


def test_get_editor_prompt_without_config(config_service):
    assert config_service.get_editor_prompt() == "You are a creative writing editor"


def test_get_writer_name_with_config(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.get_writer_name() == "Test Writer"


def test_get_writer_name_without_config(config_service):
    assert config_service.get_writer_name() == "Writer"


def test_get_writer_prompt_with_config(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.get_writer_prompt() == "Testing persona for writer"


def test_get_writer_prompt_without_config(config_service):
    assert config_service.get_writer_prompt() == "You are a creative writer"


def test_get_publisher_name_with_config(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.get_publisher_name() == "Test Publisher"


def test_get_publisher_name_without_config(config_service):
    assert config_service.get_publisher_name() == "Publisher"


def test_get_publisher_prompt_with_config(config_service, mock_file_read):
    config_service.initialize_config()
    assert config_service.get_publisher_prompt() == "Testing persona for publisher"


def test_get_publisher_prompt_without_config(config_service):
    assert config_service.get_publisher_prompt() == "You are a publisher"
