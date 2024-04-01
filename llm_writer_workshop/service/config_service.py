import logging
import toml
from flask import current_app

logger = logging.getLogger(__name__)

data = {}


def initialize_config():
    with open("config/config.toml", "r") as file:
        data = toml.load(file)

    logger.info(data)


def get_agent_name():
    try:
        return data["agent_config"]["name"]
    except KeyError:
        return "Agent"


def get_agent_prompt():
    try:
        return data["agent_config"]["persona"]
    except KeyError:
        return "You are a creative writing agent"


def get_editor_name():
    try:
        return data["editor_config"]["name"]
    except KeyError:
        return "Editor"


def get_editor_prompt():
    try:
        return data["editor_config"]["persona"]
    except KeyError:
        return "You are a creative writing editor"


def get_writer_name():
    try:
        return data["writer_config"]["name"]
    except KeyError:
        return "Writer"


def get_writer_prompt():
    try:
        return data["writer_config"]["persona"]
    except KeyError:
        return "You are a creative writer"


def get_publisher_name():
    try:
        return data["publisher_config"]["name"]
    except KeyError:
        return "Publisher"


def get_publisher_prompt():
    try:
        return data["publisher_config"]["persona"]
    except KeyError:
        return "You are a publisher"
