from llm_writer_workshop.chatter.chatter_factory import ChatterFactory
from ..chatter.mistral_chatter import MistralChatter
from ..chatter.openai_chatter import OpenAIChatter
from ..service.config_service import ConfigService
import logging

logger = logging.getLogger(__name__)


class ChatService:

    def __init__(self, config_service: ConfigService):
        self.config_service = config_service

    def chat(self, text, role, model):
        try:
            chatter_factory = ChatterFactory()
            chatter = chatter_factory.get_chatter(role, model)

            request = (
                "Here is the original writing for critique: \n***" + text + "\n***\n"
            )

            review = chatter.chat(request)

            return {"review": review, "role": role}

        except Exception as e:
            logger.error(e)
            return "I'm sorry, I'm having trouble processing your request. Please try again later."
