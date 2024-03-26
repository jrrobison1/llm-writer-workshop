import os
from openai import OpenAI

DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_MAX_OUTPUT_TOKENS = 512
DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant"
DEFAULT_TEMPERATURE = 1


class OpenAIChatter:
    def __init__(
        self,
        *,
        model=DEFAULT_MODEL,
        system_prompt=DEFAULT_SYSTEM_PROMPT,
        name,
        max_output_tokens=DEFAULT_SYSTEM_PROMPT
    ):
        self.model = model
        self.max_output_tokens = max_output_tokens
        self.name = name
        self.initial_prompt = {"role": "system", "content": system_prompt}
        self.message_history = []
        self.message_history.append(self.initial_prompt)
        self.openai_api_key = os.environ.get("OPENAI_API_KEY")
        self.open_ai_client = OpenAI(api_key=self.openai_api_key)

    def chat(self, message):
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

    def add_to_history(self, message):
        user_message = {"role": "user", "content": message}
        self.message_history.append(user_message)
