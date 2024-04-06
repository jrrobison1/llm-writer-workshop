import logging
import toml

logger = logging.getLogger(__name__)


class ConfigService:
    def __init__(self):
        self.data = {}

    def initialize_config(self):
        with open("config/config.toml", "r") as file:
            logger.debug("Loading config file")
            self.data = toml.load(file)

    def get_agent_name(self):
        try:
            return self.data["agent_config"]["name"]
        except KeyError as e:
            logger.error(e)
            return "Agent"

    def get_agent_prompt(self):
        try:
            return self.data["agent_config"]["persona"]
        except KeyError:
            return "You are a creative writing agent"

    def get_editor_name(self):
        try:
            return self.data["editor_config"]["name"]
        except KeyError:
            return "Editor"

    def get_editor_prompt(self):
        try:
            return self.data["editor_config"]["persona"]
        except KeyError:
            return "You are a creative writing editor"

    def get_writer_name(self):
        try:
            return self.data["writer_config"]["name"]
        except KeyError:
            return "Writer"

    def get_writer_prompt(self):
        try:
            return self.data["writer_config"]["persona"]
        except KeyError:
            return "You are a creative writer"

    def get_publisher_name(self):
        try:
            return self.data["publisher_config"]["name"]
        except KeyError:
            return "Publisher"

    def get_publisher_prompt(self):
        try:
            return self.data["publisher_config"]["persona"]
        except KeyError:
            return "You are a publisher"
