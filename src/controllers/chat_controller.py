from flask import Blueprint, request, jsonify
from multi_model_writer_workshop import luis_chatter

chat_bp = Blueprint("chat", __name__, url_prefix="/chat")


@chat_bp.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    text = data["text"]

    feedbacks = luis_chatter.chat(text)
    return jsonify({"feedbacks": feedbacks})
