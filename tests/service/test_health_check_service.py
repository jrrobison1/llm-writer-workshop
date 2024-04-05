from pytest import fixture
from llm_writer_workshop.service.health_check_service import HealthCheckService


@fixture
def health_check_service():
    return HealthCheckService()


def test_health_check(health_check_service):
    expected = ("", 200)
    actual = health_check_service.health_check()

    assert actual == expected
