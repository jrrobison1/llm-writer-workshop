from flask import Blueprint, jsonify
from injector import inject
from ..service.chat_service import ChatService
import logging
from ..schema.chat_request import ChatRequest
from webargs.flaskparser import use_kwargs

logger = logging.getLogger(__name__)
chat_bp = Blueprint("chat", __name__, url_prefix="/api/v1")


@chat_bp.route("/generate-reviews", methods=["POST"])
@inject
@use_kwargs(ChatRequest, location="json")
def generate_reviews(chat_service: ChatService, **chat_request: ChatRequest):
    """
    Generate reviews based on the provided chat request.

    This endpoint handles POST requests to generate reviews using the ChatService.
    It expects a JSON payload conforming to the ChatRequest schema.

    Args:
        chat_service (ChatService): An injected instance of the ChatService.
        **chat_request (ChatRequest): Keyword arguments representing the chat request data.

    Returns:
        flask.Response: A JSON response containing the generated feedbacks.
        If an error occurs, it returns a JSON error message with a 500 status code.

    Raises:
        Exception: Any exception that occurs during the review generation process.
    """
    try:
        feedbacks = chat_service.chat_all(chat_request)
        logger.debug(feedbacks)
        data_return = jsonify(feedbacks)
        return data_return
    except Exception as e:
        logger.fatal(e)
        return jsonify({"error_message": "An server error has occurred"}), 500
