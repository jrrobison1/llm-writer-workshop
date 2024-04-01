from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    load_dotenv(override=True)
    CORS(app)

    with app.app_context():
        from llm_writer_workshop.controller.chat_controller import chat_bp
        from llm_writer_workshop.controller.health_check_controller import health_bp
        from llm_writer_workshop.service import config_service

        app.register_blueprint(chat_bp)
        app.register_blueprint(health_bp)

        config_service.initialize_config()

    return app


if __name__ == "__main__":
    create_app().run()
