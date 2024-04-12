import logging


logger = logging.getLogger(__name__)


class HealthCheckService:
    def health_check(self):
        logger.debug("Health check called")
        return "", 200
