from injector import Module, provider, singleton
from llm_writer_workshop.service.chat_service import ChatService
from llm_writer_workshop.service.config_service import ConfigService
from llm_writer_workshop.service.health_check_service import HealthCheckService


class AppModule(Module):
    @singleton
    @provider
    def provide_chat_service(self, configService: ConfigService) -> ChatService:
        return ChatService(configService)

    @singleton
    @provider
    def provide_config_service(self) -> ConfigService:
        return ConfigService()

    @singleton
    @provider
    def provide_health_check_service(self) -> HealthCheckService:
        return HealthCheckService()
