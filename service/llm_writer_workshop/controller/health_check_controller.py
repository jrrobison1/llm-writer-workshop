from flask import Blueprint, jsonify
from injector import inject
from ..service.health_check_service import HealthCheckService

health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("", methods=["GET", "HEAD"])
@inject
def health_check(health_check_service: HealthCheckService):
    try:
        return jsonify(health_check_service.health_check())
    except Exception as e:
        return jsonify({"error_message": "An server error has occurred"}), 500
