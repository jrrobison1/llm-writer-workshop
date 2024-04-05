from llm_writer_workshop.chatter.gemini_chatter import GeminiChatter
from llm_writer_workshop.chatter.mistral_chatter import MistralChatter
from llm_writer_workshop.chatter.openai_chatter import OpenAIChatter
from llm_writer_workshop.service.config_service import ConfigService


class ChatterFactory:
    def get_chatter(self, role, model):
        config_service = ConfigService()
        if role == "Editor":
            name = config_service.get_editor_name()
            system_prompt = config_service.get_editor_prompt()
        elif role == "Agent":
            name = config_service.get_agent_name()
            system_prompt = config_service.get_agent_prompt()
        elif role == "Writer":
            name = config_service.get_writer_name()
            system_prompt = config_service.get_writer_prompt()
        elif role == "Publisher":
            name = config_service.get_publisher_name()
            system_prompt = config_service.get_publisher_prompt()

        if model == "gpt-3.5-turbo" or model == "gpt-4":
            return OpenAIChatter(
                model=model,
                system_prompt=system_prompt,
                name=name,
                max_output_tokens=512,
            )
        elif model == "gemini-pro":
            return GeminiChatter(
                model=model,
                system_prompt=system_prompt,
                name=name,
                max_output_tokens=512,
            )
        elif (
            model == "mistral-small"
            or model == "mistral-medium"
            or model == "mistral-large"
        ):
            return MistralChatter(
                model=model,
                system_prompt=system_prompt,
                name=name,
                max_output_tokens=512,
            )
        else:
            raise ValueError("Invalid model")
