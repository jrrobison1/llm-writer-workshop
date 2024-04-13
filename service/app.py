import logging
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_injector import FlaskInjector
from di import AppModule
from llm_writer_workshop.service.config_service import ConfigService
from llm_writer_workshop.controller.chat_controller import chat_bp
from llm_writer_workshop.controller.health_check_controller import health_bp


def create_app():
    app = Flask(__name__)
    logging.basicConfig(level=logging.DEBUG)
    CORS(app)
    load_dotenv(override=True)

    app.register_blueprint(chat_bp)
    app.register_blueprint(health_bp)

    FlaskInjector(app=app, modules=[AppModule()])

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
