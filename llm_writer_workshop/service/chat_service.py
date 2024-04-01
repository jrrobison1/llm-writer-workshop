from ..chatter.mistral_chatter import MistralChatter
from ..chatter.openai_chatter import OpenAIChatter
from . import config_service
import logging

logger = logging.getLogger(__name__)


writer_chatter = OpenAIChatter(
    model="gpt-3.5-turbo",
    system_prompt=config_service.get_writer_prompt(),
    name=config_service.get_writer_name(),
    max_output_tokens=512,
)
editor_chatter = MistralChatter(
    model="mistral-small",
    system_prompt=config_service.get_editor_prompt(),
    name=config_service.get_editor_name(),
    max_output_tokens=512,
)
agent_chatter = OpenAIChatter(
    model="gpt-3.5-turbo",
    system_prompt=config_service.get_agent_prompt(),
    name=config_service.get_agent_name(),
    max_output_tokens=512,
)
publisher_chatter = OpenAIChatter(
    model="gpt-3.5-turbo",
    system_prompt=config_service.get_publisher_prompt(),
    name=config_service.get_publisher_name(),
    max_output_tokens=1024,
)


def chat(text):
    try:
        request = (
            "Here is the original writing for critique, written by User: \n***"
            + text
            + "\n***\n"
        )
        editor_feedback = editor_chatter.chat(request)
        editor_template = (
            "Here is what Luis thinks about the original writing: \n***\n"
            + editor_feedback
            + "\n***\n"
        )

        agent_chatter.add_to_history(editor_template)
        agent_chatter.add_to_history(request)
        agent_feedback = agent_chatter.chat("")
        agent_template = (
            "Here is what Heidi thinks about the original writing: \n***\n"
            + agent_feedback
            + "\n***\n"
        )

        writer_chatter.add_to_history(editor_template)
        writer_chatter.add_to_history(agent_template)
        writer_chatter.add_to_history(request)
        writer_feedback = writer_chatter.chat("")

        publisher_feedback = publisher_chatter.chat(request)

        return [
            {"text": editor_feedback, "model": "GPT-4", "role": "editor"},
            {"text": agent_feedback, "model": "GPT-4", "role": "agent"},
            {"text": writer_feedback, "model": "GPT-4", "role": "writer"},
            {"text": publisher_feedback, "model": "GPT-4", "role": "publisher"},
        ]
    except Exception as e:
        logger.error(e)
        return "I'm sorry, I'm having trouble processing your request. Please try again later."
