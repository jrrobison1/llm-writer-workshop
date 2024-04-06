import logging
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

from llm_writer_workshop.chatter.chatter import Chatter

logger = logging.getLogger(__name__)


class GeminiChatter(Chatter):
    DEFAULT_MODEL = "gemini-pro"
    DEFAULT_MAX_OUTPUT_TOKENS = 512
    DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant"
    DEFAULT_TEMPERATURE = 1.0

    def __init__(
        self,
        *,
        model=DEFAULT_MODEL,
        system_prompt=DEFAULT_SYSTEM_PROMPT,
        max_output_tokens=DEFAULT_MAX_OUTPUT_TOKENS,
        temperature=DEFAULT_TEMPERATURE,
        name
    ):
        self.max_output_tokens = max_output_tokens
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt
        self.message_history = []
        self.name = name

    def chat(self, message):
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

    def add_to_history(self, message):
        pass
