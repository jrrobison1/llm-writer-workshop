import logging
import os
from typing import List

import google.generativeai as genai
from google.generativeai.types import HarmBlockThreshold, HarmCategory

from llm_writer_workshop.chatter.chatter import Chatter

logger = logging.getLogger(__name__)


class GeminiChatter(Chatter):
    """
    A class for interacting with Google's Gemini AI models.

    This class implements the Chatter interface and provides methods for
    initializing a chat session and sending messages to the Gemini model.
    """

    DEFAULT_MODEL = "gemini-pro"
    DEFAULT_MAX_OUTPUT_TOKENS = 512
    DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant"
    DEFAULT_TEMPERATURE = 1.0

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
        Initialize the GeminiChatter.

        Args:
            model (str): The Gemini AI model to use. Defaults to DEFAULT_MODEL.
            system_prompt (str): The initial system prompt. Defaults to DEFAULT_SYSTEM_PROMPT.
            max_output_tokens (int): Maximum number of tokens in the output. Defaults to DEFAULT_MAX_OUTPUT_TOKENS.
            temperature (float): The temperature for response generation. Defaults to DEFAULT_TEMPERATURE.
            name (str): The name of the chatter.
        """
        self.max_output_tokens = max_output_tokens
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt
        self.message_history: List[str] = []
        self.name = name

    def chat(self, message: str) -> str:
        """
        Send a message to the Gemini AI model and get a response.

        Args:
            message (str): The user's message to send to the model.

        Returns:
            str: The AI's response message.
        """
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel(self.model)

        response = model.generate_content(
            message,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                max_output_tokens=self.max_output_tokens,
                temperature=self.temperature,
            ),
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            },
        )

        return response.text

    def add_to_history(self, message: str) -> None:
        """
        Add a message to the conversation history.

        This method is currently not implemented for GeminiChatter.

        Args:
            message (str): The message to add to the history.
        """
        pass
