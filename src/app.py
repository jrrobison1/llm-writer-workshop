from flask import Flask, request, jsonify
from multi_model_writer_workshop import arthur_chatter, luis_chatter, heidi_chatter
from controllers.health_controller import health_bp
from controllers.chat_controller import chat_bp

app = Flask(__name__)
app.register_blueprint(health_bp)
app.register_blueprint(chat_bp)


if __name__ == "__main__":
    app.run()
