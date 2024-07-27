import os
from typing import List

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

from llm_writer_workshop.chatter.chatter import Chatter

class MistralChatter(Chatter):
    """
    A class for interacting with Mistral AI's chat models.

    This class implements the Chatter interface and provides methods for
    initializing a chat session, sending messages, and managing conversation history.
    """

    DEFAULT_MODEL = "mistral-small"
    DEFAULT_MAX_OUTPUT_TOKENS = 512
    DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant"
    DEFAULT_TEMPERATURE = 0.7

    def __init__(
        self,
        *,
        model: str = DEFAULT_MODEL,
        system_prompt: str = DEFAULT_SYSTEM_PROMPT,
        max_output_tokens: int = DEFAULT_MAX_OUTPUT_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        name: str
    ):
        """
        Initialize the MistralChatter.

        Args:
            model (str): The Mistral AI model to use. Defaults to DEFAULT_MODEL.
            system_prompt (str): The initial system prompt. Defaults to DEFAULT_SYSTEM_PROMPT.
            max_output_tokens (int): Maximum number of tokens in the output. Defaults to DEFAULT_MAX_OUTPUT_TOKENS.
            temperature (float): The temperature for response generation. Defaults to DEFAULT_TEMPERATURE.
            name (str): The name of the chatter.
        """
        try:
            self.mistral_api_key = os.environ.get("MISTRAL_API_KEY")
            self.model = model
            self.max_output_tokens = max_output_tokens
            self.temperature = temperature
            self.name = name
            self.message_history: List[ChatMessage] = []
            self.client = MistralClient(api_key=self.mistral_api_key)
            self.initial_prompt = ChatMessage(role="system", content=system_prompt)
            self.message_history.append(self.initial_prompt)
        except Exception as e:
            print(e)

    def chat(self, message: str) -> str:
        """
        Send a message to the Mistral AI chat model and get a response.

        Args:
            message (str): The user's message to send to the model.

        Returns:
            str: The AI's response message.
        """
        if message != "":
            user_message = ChatMessage(role="user", content=message)
            self.message_history.append(user_message)

        ai_messsage = ""
        for chunk in self.client.chat_stream(
            model=self.model,
            messages=self.message_history,
            max_tokens=self.max_output_tokens,
            temperature=self.temperature,
        ):
            if (
                chunk.choices[0].delta.content is not None
                and chunk.choices[0].delta.content != ""
            ):
                ai_messsage += chunk.choices[0].delta.content

        self.message_history.append(ChatMessage(role="assistant", content=ai_messsage))

        return ai_messsage

    def add_to_history(self, message: str) -> None:
        """
        Add a user message to the conversation history.

        Args:
            message (str): The user's message to add to the history.
        """
        user_message = ChatMessage(role="user", content=message)
        self.message_history.append(user_message)
