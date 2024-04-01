from flask import Blueprint, request, jsonify
from ..service import chat_service
import logging

logger = logging.getLogger(__name__)


chat_bp = Blueprint("chat", __name__, url_prefix="/api/v1")


@chat_bp.route("/generate-reviews", methods=["POST"])
def submit():
    logger.info(request.get_json())

    if (
        request.is_json is False
        or request.get_json() is None
        or request.get_json().get("text") is None
    ):
        return jsonify({"error_message": "Empty JSON"}), 400

    data = request.get_json()
    text = data["text"]

    try:
        feedbacks = chat_service.chat(text)
        return jsonify(feedbacks)
    except Exception:
        return jsonify({"error_message": "An server error has occurred"}), 500
