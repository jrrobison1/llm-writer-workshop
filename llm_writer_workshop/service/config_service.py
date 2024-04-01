import logging
import toml
from flask import current_app

logger = logging.getLogger(__name__)


def initialize_config():
    with open("config/config.toml", "r") as file:
        data = toml.load(file)

    current_app.config.update(data)
    logger.info(data)


def get_agent_name():
    try:
        return current_app.config["agent_config"]["name"]
    except KeyError:
        return "Agent"


def get_agent_prompt():
    try:
        return current_app.config["agent_config"]["persona"]
    except KeyError:
        return "You are a creative writing agent"


def get_editor_name():
    try:
        return current_app.config["editor_config"]["name"]
    except KeyError:
        return "Editor"


def get_editor_prompt():
    try:
        return current_app.config["editor_config"]["persona"]
    except KeyError:
        return "You are a creative writing editor"


def get_writer_name():
    try:
        return current_app.config["writer_config"]["name"]
    except KeyError:
        return "Writer"


def get_writer_prompt():
    try:
        return current_app.config["writer_config"]["persona"]
    except KeyError:
        return "You are a creative writer"


def get_publisher_name():
    try:
        return current_app.config["publisher_config"]["name"]
    except KeyError:
        return "Publisher"


def get_publisher_prompt():
    try:
        return current_app.config["publisher_config"]["persona"]
    except KeyError:
        return "You are a publisher"
