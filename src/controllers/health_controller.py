from flask import Blueprint, request, jsonify

health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("", methods=["GET", "HEAD"])
def health():
    return "", 200
