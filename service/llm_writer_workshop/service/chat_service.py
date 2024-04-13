from llm_writer_workshop.chatter.chatter_factory import ChatterFactory
from ..chatter.mistral_chatter import MistralChatter
from ..chatter.openai_chatter import OpenAIChatter
from ..service.config_service import ConfigService
from ..schema.chat_request import ChatRequest
import concurrent.futures
import logging

logger = logging.getLogger(__name__)


class ChatService:

    def __init__(self, chatter_factory: ChatterFactory):
        self.chatter_factory = chatter_factory

    def chat(self, text, role, model):
        try:
            chatter = self.chatter_factory.get_chatter(role, model)
            request = (
                "Here is the original writing for critique: \n***" + text + "\n***\n"
            )

            review = chatter.chat(request)

            logger.debug(f"Review: {review}, Role: {role}")
            return {"review": review, "role": role}

        except Exception as e:
            logger.error(e)
            return "I'm sorry, I'm having trouble processing your request. Please try again later."

    def chat_all(self, chat_request: ChatRequest):
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(
                        self.chat,
                        chat_request["text"],
                        model["role"],
                        model["model"],
                    )
                    for model in chat_request["models"]
                ]
                feedbacks = [future.result() for future in futures]
            logger.debug(feedbacks)
            return feedbacks
        except Exception as e:
            logger.fatal(e)
            return "An server error has occurred"
