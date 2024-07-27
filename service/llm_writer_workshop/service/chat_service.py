from typing import Dict, List, Union
from llm_writer_workshop.chatter.chatter_factory import ChatterFactory
from ..schema.chat_request import ChatRequest
import concurrent.futures
import logging

logger = logging.getLogger(__name__)


class ChatService:
    """
    A service class for handling chat operations.
    """

    def __init__(self, chatter_factory: ChatterFactory):
        """
        Initialize the ChatService with a ChatterFactory.

        Args:
            chatter_factory (ChatterFactory): A factory for creating chatters.
        """
        self.chatter_factory = chatter_factory

    def chat(self, text: str, role: str, model: str) -> Dict[str, str]:
        """
        Process a single chat request.

        Args:
            text (str): The text to be critiqued.
            role (str): The role of the chatter.
            model (str): The model to be used for chatting.

        Returns:
            Dict[str, str]: A dictionary containing the review and role.
        """
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

    def chat_all(self, chat_request: ChatRequest) -> Union[List[Dict[str, str]], str]:
        """
        Process multiple chat requests concurrently.

        Args:
            chat_request (ChatRequest): The chat request containing text and models.

        Returns:
            Union[List[Dict[str, str]], str]: A list of feedback dictionaries or an error message.
        """
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
