import os
import google.generativeai as genai


class GeminiChatter:
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
        self.gemini_api_key = os.environ.get("GEMINI_API_KEY")
        genai.configure(api_key=self.gemini_api_key)

        self.max_output_tokens = max_output_tokens
        self.temperature = temperature
        self.model = model
        self.gemini_model = genai.GenerativeModel(self.model)
        self.gemini_model.system_prompt = system_prompt
        self.message_history = []
        self.name = name

    def chat(self, message):
        if message != "":
            user_message = {"role": "user", "parts": [message]}
            self.message_history.append(user_message)
        # print(self.message_history)

        for message in self.message_history:
            print(message["role"])

        response = self.gemini_model.generate_content(
            self.message_history,
            stream=True,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                # stop_sequences=['x'],
                max_output_tokens=self.max_output_tokens,
                temperature=self.temperature,
            ),
        )

        ai_message = ""
        for chunk in response:
            if (
                chunk.candidates is not None
                and chunk.candidates[0].content is not None
                and chunk.candidates[0].content.parts is not None
                and len(chunk.candidates[0].content.parts) > 0
            ):
                response_text = (
                    chunk.candidates[0].content.parts[0].text.replace("•", "  *")
                )
                ai_message += response_text

        self.message_history.append({"role": "model", "parts": [ai_message]})

        return ai_message

    def add_to_history(self, message):
        if self.message_history is not None:
            if len(self.message_history) > 0:
                last_message = self.message_history[-1]
                last_message["parts"][0] = last_message["parts"][0] + " " + message
            else:
                user_message = {"role": "user", "parts": [message]}
                self.message_history.append(user_message)
