import logging
import os
from typing import Dict, Any

from anthropic import Anthropic

from llm_writer_workshop.chatter.chatter import Chatter

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "claude-3-haiku-20240307"
DEFAULT_MAX_OUTPUT_TOKENS = 512
DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant"
DEFAULT_TEMPERATURE = 1


class ClaudeChatter(Chatter):
    """
    A class for interacting with the Claude AI model using the Anthropic API.
    """

    def __init__(
        self,
        *,
        model: str = DEFAULT_MODEL,
        system_prompt: str = DEFAULT_SYSTEM_PROMPT,
        name: str,
        max_output_tokens: int = DEFAULT_SYSTEM_PROMPT
    ):
        """
        Initialize the ClaudeChatter instance.

        Args:
            model (str): The Claude model to use. Defaults to DEFAULT_MODEL.
            system_prompt (str): The initial system prompt. Defaults to DEFAULT_SYSTEM_PROMPT.
            name (str): The name of the chatter instance.
            max_output_tokens (int): The maximum number of tokens in the output. Defaults to DEFAULT_SYSTEM_PROMPT.
        """
        try:
            self.model = model
            self.max_output_tokens = max_output_tokens
            self.name = name
            self.initial_prompt = system_prompt
            self.message_history = []
            self.api_key = os.environ.get("ANTHROPIC_API_KEY")
        except Exception as e:
            print(e)

    def chat(self, message: str) -> str:
        """
        Send a message to the Claude AI and get a response.

        Args:
            message (str): The message to send to the AI.

        Returns:
            str: The AI's response.
        """
        client = Anthropic(api_key=self.api_key)
        if message != "":
            self.add_to_history({"role": "user", "content": message})

        try:
            response = client.messages.create(
                model=self.model,
                system=self.initial_prompt,
                max_tokens=self.max_output_tokens,
                messages=[{"role": "user", "content": message}],
            )
        except Exception as e:
            logger.error(e)

        return response.content[0].text

    def add_to_history(self, message: Dict[str, str]) -> None:
        """
        Add a message to the conversation history.

        Args:
            message (Dict[str, str]): The message to add to the history.
        """
        user_message = {"role": "user", "content": message}
        self.message_history.append(user_message)
