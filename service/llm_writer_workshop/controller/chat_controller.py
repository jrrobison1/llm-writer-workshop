from flask import Blueprint, request, jsonify
from injector import inject
from ..service.chat_service import ChatService
import logging
import concurrent.futures

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
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(chat_service.chat, text, model["role"], model["model"])
                for model in data["models"]
            ]
            feedbacks = [future.result() for future in futures]
        logger.debug(feedbacks)
        data_return = jsonify(feedbacks)
        return data_return
    except Exception as e:
        logger.fatal(e)
        return jsonify({"error_message": "An server error has occurred"}), 500
