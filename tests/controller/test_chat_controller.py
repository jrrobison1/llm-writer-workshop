import pytest
from app import create_app  # Adjust the import according to your application structure


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_generate_reviews_success(client, mocker):
    mocker.patch(
        "llm_writer_workshop.service.chat_service.ChatService.chat",
        return_value={"feedback": "Positive"},
    )
    response = client.post(
        "/api/v1/generate-reviews", json={"text": "This is a sample review text"}
    )
    assert response.status_code == 200
    assert response.json == {"feedback": "Positive"}


def test_generate_reviews_no_json(client):
    response = client.post("/api/v1/generate-reviews", data="This is not a JSON")
    assert response.status_code == 415


def test_generate_reviews_empty_json(client):
    response = client.post("/api/v1/generate-reviews", json={})
    assert response.status_code == 400
    assert "Empty JSON" in response.json["error_message"]


def test_generate_reviews_missing_text_field(client):
    response = client.post(
        "/api/v1/generate-reviews", json={"not_text": "This should fail"}
    )
    assert response.status_code == 400
    assert "Empty JSON" in response.json["error_message"]


def test_generate_reviews_server_error(client, mocker):
    mocker.patch(
        "llm_writer_workshop.service.chat_service.ChatService.chat",
        side_effect=Exception("Unexpected error"),
    )
    response = client.post(
        "/api/v1/generate-reviews", json={"text": "This will trigger a server error"}
    )
    assert response.status_code == 500
    assert "An server error has occurred" in response.json["error_message"]
