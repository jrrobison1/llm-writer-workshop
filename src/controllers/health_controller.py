from flask import Blueprint, request, jsonify
from services import health_service

health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("", methods=["GET", "HEAD"])
def health():
    return health_service.health_check()
