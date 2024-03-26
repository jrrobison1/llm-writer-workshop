from flask import Blueprint, request, jsonify
from ..service import chat_service

chat_bp = Blueprint("chat", __name__, url_prefix="/chat")


@chat_bp.route("/submit", methods=["POST"])
def submit():
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
        return jsonify({"feedbacks": feedbacks})
    except Exception:
        return jsonify({"error_message": "An server error has occurred"}), 500
