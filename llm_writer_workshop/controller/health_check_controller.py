from flask import Blueprint, jsonify
from injector import inject
from ..service.health_check_service import HealthCheckService

health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("", methods=["GET", "HEAD"])
@inject
def health_check(health_check_service: HealthCheckService):
    return jsonify(health_check_service.health_check())
