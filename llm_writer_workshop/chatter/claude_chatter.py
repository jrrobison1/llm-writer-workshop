import logging
import os

from anthropic import Anthropic

from llm_writer_workshop.chatter.chatter import Chatter

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "claude-3-haiku-20240307"
DEFAULT_MAX_OUTPUT_TOKENS = 512
DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant"
DEFAULT_TEMPERATURE = 1


class ClaudeChatter(Chatter):
    def __init__(
        self,
        *,
        model=DEFAULT_MODEL,
        system_prompt=DEFAULT_SYSTEM_PROMPT,
        name,
        max_output_tokens=DEFAULT_SYSTEM_PROMPT
    ):
        try:
            self.model = model
            self.max_output_tokens = max_output_tokens
            self.name = name
            self.initial_prompt = system_prompt
            self.message_history = []
            self.api_key = os.environ.get("ANTHROPIC_API_KEY")
        except Exception as e:
            print(e)

    def chat(self, message):
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

    def add_to_history(self, message):
        user_message = {"role": "user", "content": message}
        self.message_history.append(user_message)
