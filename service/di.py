from injector import Module, provider, singleton

from llm_writer_workshop.chatter.chatter_factory import ChatterFactory
from llm_writer_workshop.service.chat_service import ChatService
from llm_writer_workshop.service.config_service import ConfigService
from llm_writer_workshop.service.health_check_service import HealthCheckService


class AppModule(Module):

    @singleton
    @provider
    def provide_config_service(self) -> ConfigService:
        config_service = ConfigService()
        config_service.initialize_config()
        return config_service

    @singleton
    @provider
    def provide_chatter_factory(self, config_service: ConfigService) -> ChatterFactory:
        return ChatterFactory(config_service)

    @singleton
    @provider
    def provide_chat_service(self, chatter_factory: ChatterFactory) -> ChatService:
        return ChatService(chatter_factory)

    @singleton
    @provider
    def provide_health_check_service(self) -> HealthCheckService:
        return HealthCheckService()
