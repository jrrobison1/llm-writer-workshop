import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_health_check_success_get(client, mocker):
    mocker.patch(
        "llm_writer_workshop.service.health_check_service.HealthCheckService.health_check",
        return_value=("Return text", 200),
    )
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == ["Return text", 200]


def test_health_check_success_head(client, mocker):
    mocker.patch(
        "llm_writer_workshop.service.health_check_service.HealthCheckService.health_check",
        return_value=("Return text", 200),
    )
    response = client.head("/health")
    assert response.status_code == 200


def test_health_check_server_error(client, mocker):
    mocker.patch(
        "llm_writer_workshop.service.health_check_service.HealthCheckService.health_check",
        side_effect=Exception("Unexpected error"),
    )
    response = client.get("/health")
    assert response.status_code == 500
    assert "An server error has occurred" in response.json["error_message"]
