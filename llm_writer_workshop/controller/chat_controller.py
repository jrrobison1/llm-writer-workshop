from flask import Blueprint, request, jsonify
from injector import inject
from ..service.chat_service import ChatService
import logging

logger = logging.getLogger(__name__)
chat_bp = Blueprint("chat", __name__, url_prefix="/api/v1")


@chat_bp.route("/generate-reviews", methods=["POST"])
@inject
def generate_reviews(chat_service: ChatService):
    if (
        request.is_json is False
        or request.get_json() is None
        or request.get_json().get("text") is None
    ):
        return jsonify({"error_message": "Empty JSON"}), 400

    data = request.get_json()
    text = data["text"]

    try:
        feedbacks = []
        for model in data["models"]:
            feedback = chat_service.chat(text, model["role"], model["model"])
            feedbacks.append(feedback)
        data_return = jsonify(feedbacks)
        return data_return
    except Exception as e:
        logger.fatal(e)
        return jsonify({"error_message": "An server error has occurred"}), 500
