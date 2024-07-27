import logging
import toml

logger = logging.getLogger(__name__)


class ConfigService:
    """
    A service class for managing configuration settings.
    """

    def __init__(self):
        """
        Initialize the ConfigService with an empty data dictionary.
        """
        self.data = {}

    def initialize_config(self):
        """
        Load configuration data from a TOML file.
        """
        with open("config/config.toml", "r") as file:
            logger.debug("Loading config file")
            self.data = toml.load(file)

    def get_agent_name(self):
        """
        Get the agent's name from the configuration.

        Returns:
            str: The agent's name or "Agent" if not found.
        """
        try:
            return self.data["agent_config"]["name"]
        except KeyError as e:
            logger.error(e)
            return "Agent"

    def get_agent_prompt(self):
        """
        Get the agent's prompt from the configuration.

        Returns:
            str: The agent's prompt or a default prompt if not found.
        """
        try:
            return self.data["agent_config"]["persona"]
        except KeyError:
            return "You are a creative writing agent"

    def get_editor_name(self):
        """
        Get the editor's name from the configuration.

        Returns:
            str: The editor's name or "Editor" if not found.
        """
        try:
            return self.data["editor_config"]["name"]
        except KeyError:
            return "Editor"

    def get_editor_prompt(self):
        """
        Get the editor's prompt from the configuration.

        Returns:
            str: The editor's prompt or a default prompt if not found.
        """
        try:
            return self.data["editor_config"]["persona"]
        except KeyError:
            return "You are a creative writing editor"

    def get_writer_name(self):
        """
        Get the writer's name from the configuration.

        Returns:
            str: The writer's name or "Writer" if not found.
        """
        try:
            return self.data["writer_config"]["name"]
        except KeyError:
            return "Writer"

    def get_writer_prompt(self):
        """
        Get the writer's prompt from the configuration.

        Returns:
            str: The writer's prompt or a default prompt if not found.
        """
        try:
            return self.data["writer_config"]["persona"]
        except KeyError:
            return "You are a creative writer"

    def get_publisher_name(self):
        """
        Get the publisher's name from the configuration.

        Returns:
            str: The publisher's name or "Publisher" if not found.
        """
        try:
            return self.data["publisher_config"]["name"]
        except KeyError:
            return "Publisher"

    def get_publisher_prompt(self):
        """
        Get the publisher's prompt from the configuration.

        Returns:
            str: The publisher's prompt or a default prompt if not found.
        """
        try:
            return self.data["publisher_config"]["persona"]
        except KeyError:
            return "You are a publisher"
