import os
from typing import Dict
from openai import OpenAI

from llm_writer_workshop.chatter.chatter import Chatter

DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_MAX_OUTPUT_TOKENS = 768
DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant"
DEFAULT_TEMPERATURE = 1

class OpenAIChatter(Chatter):
    """
    A class for interacting with OpenAI's chat models.

    This class implements the Chatter interface and provides methods for
    initializing a chat session, sending messages, and managing conversation history.
    """

    def __init__(
        self,
        *,
        model: str = DEFAULT_MODEL,
        system_prompt: str = DEFAULT_SYSTEM_PROMPT,
        name: str,
        max_output_tokens: int = DEFAULT_MAX_OUTPUT_TOKENS
    ):
        """
        Initialize the OpenAIChatter.

        Args:
            model (str): The OpenAI model to use. Defaults to DEFAULT_MODEL.
            system_prompt (str): The initial system prompt. Defaults to DEFAULT_SYSTEM_PROMPT.
            name (str): The name of the chatter.
            max_output_tokens (int): Maximum number of tokens in the output. Defaults to DEFAULT_MAX_OUTPUT_TOKENS.
        """
        try:
            self.model = model
            self.max_output_tokens = max_output_tokens
            self.name = name
            self.initial_prompt = {"role": "system", "content": system_prompt}
            self.message_history = []
            self.message_history.append(self.initial_prompt)
            self.openai_api_key = os.environ.get("OPENAI_API_KEY")
            self.open_ai_client = OpenAI(api_key=self.openai_api_key)
        except Exception as e:
            print(e)

    def chat(self, message: str) -> str:
        """
        Send a message to the OpenAI chat model and get a response.

        Args:
            message (str): The user's message to send to the model.

        Returns:
            str: The AI's response message.
        """
        user_message = {}
        if message != "":
            user_message = {"role": "user", "content": message}
            self.message_history.append(user_message)

        # Streaming
        openai_stream = self.open_ai_client.chat.completions.create(
            model=self.model,
            messages=self.message_history,
            max_tokens=self.max_output_tokens,
            temperature=DEFAULT_TEMPERATURE,
            stream=True,
        )

        ai_messsage = ""
        for openai_chunk in openai_stream:
            if openai_chunk.choices[0].delta.content is not None:
                ai_messsage += openai_chunk.choices[0].delta.content

        return ai_messsage

    def add_to_history(self, message: str) -> None:
        """
        Add a user message to the conversation history.

        Args:
            message (str): The user's message to add to the history.
        """
        user_message: Dict[str, str] = {"role": "user", "content": message}
        self.message_history.append(user_message)
