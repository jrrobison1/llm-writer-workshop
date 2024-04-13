from llm_writer_workshop.chatter.gemini_chatter import GeminiChatter
from llm_writer_workshop.chatter.mistral_chatter import MistralChatter
from llm_writer_workshop.chatter.openai_chatter import OpenAIChatter
from llm_writer_workshop.service.config_service import ConfigService
from llm_writer_workshop.chatter.claude_chatter import ClaudeChatter


class ChatterFactory:
    def __init__(self, config_service: ConfigService):
        self.config_service = config_service

    def get_chatter(self, role, model):
        if role == "Editor":
            name = self.config_service.get_editor_name()
            system_prompt = self.config_service.get_editor_prompt()
        elif role == "Agent":
            name = self.config_service.get_agent_name()
            system_prompt = self.config_service.get_agent_prompt()
        elif role == "Writer":
            name = self.config_service.get_writer_name()
            system_prompt = self.config_service.get_writer_prompt()
        elif role == "Publisher":
            name = self.config_service.get_publisher_name()
            system_prompt = self.config_service.get_publisher_prompt()

        if model == "gpt-3.5-turbo" or model == "gpt-4" or model == "gpt-4-turbo":
            return OpenAIChatter(
                model=model,
                system_prompt=system_prompt,
                name=name,
                max_output_tokens=512,
            )
        elif model == "gemini-pro" or model == "gemini-pro-1.5":
            return GeminiChatter(
                model=model,
                system_prompt=system_prompt,
                name=name,
                max_output_tokens=512,
            )
        elif (
            model == "mistral-small"
            or model == "mistral-medium"
            or model == "mistral-large-latest"
        ):
            return MistralChatter(
                model=model,
                system_prompt=system_prompt,
                name=name,
                max_output_tokens=512,
            )
        elif (
            model == "claude-3-haiku-20240307"
            or model == "claude-3-sonnet-20240229"
            or model == "claude-3-opus-20240229"
        ):
            return ClaudeChatter(
                model=model,
                system_prompt=system_prompt,
                name=name,
                max_output_tokens=512,
            )
        else:
            raise ValueError("Invalid model")
