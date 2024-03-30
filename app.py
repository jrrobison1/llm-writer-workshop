from flask import Flask
from llm_multi_model_workshop.controller.health_check_controller import health_bp
from llm_multi_model_workshop.controller.chat_controller import chat_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(health_bp)
app.register_blueprint(chat_bp)


if __name__ == "__main__":
    app.run()
