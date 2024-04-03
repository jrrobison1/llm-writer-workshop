from injector import Module, provider, singleton
from llm_writer_workshop.service.chat_service import ChatService
from llm_writer_workshop.service.config_service import ConfigService


class AppModule(Module):
    @singleton
    @provider
    def provide_chat_service(self, configService: ConfigService) -> ChatService:
        return ChatService(configService)

    @singleton
    @provider
    def provide_config_service(self) -> ConfigService:
        return ConfigService()
