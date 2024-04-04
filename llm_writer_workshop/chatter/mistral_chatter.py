import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


class MistralChatter:
    DEFAULT_MODEL = "mistral-small"
    DEFAULT_MAX_OUTPUT_TOKENS = 512
    DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant"
    DEFAULT_TEMPERATURE = 0.7

    def __init__(
        self,
        *,
        model=DEFAULT_MODEL,
        system_prompt=DEFAULT_SYSTEM_PROMPT,
        max_output_tokens=DEFAULT_MAX_OUTPUT_TOKENS,
        temperature=DEFAULT_TEMPERATURE,
        name
    ):
        try:
            self.mistral_api_key = os.environ.get("MISTRAL_API_KEY")
            self.model = model
            self.max_output_tokens = max_output_tokens
            self.temperature = temperature
            self.name = name
            self.message_history = []
            self.client = MistralClient(api_key=self.mistral_api_key)
            self.initial_prompt = ChatMessage(role="system", content=system_prompt)
            self.message_history.append(self.initial_prompt)
        except Exception as e:
            print(e)

    def chat(self, message):
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

    def add_to_history(self, message):
        user_message = ChatMessage(role="user", content=message)
        self.message_history.append(user_message)
