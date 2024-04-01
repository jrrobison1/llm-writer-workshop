from flask import Blueprint
from ..service import health_check_service

health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("", methods=["GET", "HEAD"])
def health():
    return health_check_service.health_check()
