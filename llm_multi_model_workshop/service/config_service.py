import toml

with open("config/config.toml", "r") as file:
    data = toml.load(file)

agent_config = data["agent_prompt"]
editor_config = data["editor_prompt"]
writer_config = data["writer_prompt"]
publisher_config = data["publisher_prompt"]


def get_agent_config():
    return agent_config


def get_editor_config():
    return editor_config


def get_writer_config():
    return writer_config


def get_publisher_config():
    return publisher_config
