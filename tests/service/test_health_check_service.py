import pytest
from llm_writer_workshop.service import health_check_service


class TestHealthCheckService:
    def test_health_check(self):
        expected = ("", 200)
        actual = health_check_service.health_check()

        assert actual == expected


if __name__ == "__main__":
    pytest.main()
