from pytest import fixture
from app import create_app


@fixture
def app():
    app = create_app()
    yield app


@fixture
def client(app):
    return app.test_client()


def test_generate_reviews_success(client, mocker):
    mocker.patch(
        "llm_writer_workshop.service.chat_service.ChatService.chat",
        return_value={"feedback": "Positive"},
    )

    test_json = {
        "text": "This is a sample review text",
        "models": [{"role": "Agent", "model": "gpt-3.5-turbo"}],
    }

    response = client.post("/api/v1/generate-reviews", json=test_json)
    assert response.status_code == 200
    assert response.json == [{"feedback": "Positive"}]


def test_generate_reviews_no_json(client):
    response = client.post("/api/v1/generate-reviews", data="This is not a JSON")
    assert response.status_code == 422


def test_generate_reviews_empty_json(client):
    response = client.post("/api/v1/generate-reviews", json={})
    assert response.status_code == 422


def test_generate_reviews_missing_text_field(client):
    response = client.post(
        "/api/v1/generate-reviews", json={"not_text": "This should fail"}
    )
    assert response.status_code == 422


def test_generate_reviews_server_error(client, mocker):
    mocker.patch(
        "llm_writer_workshop.service.chat_service.ChatService.chat_all",
        side_effect=Exception("Unexpected error"),
    )
    response = client.post(
        "/api/v1/generate-reviews",
        json={
            "text": "This is a sample review text",
            "models": [{"role": "Agent", "model": "gpt-3.5-turbo"}],
        },
    )
    assert response.status_code == 500
    assert "An server error has occurred" in response.json["error_message"]
