
from flask import Blueprint, request, jsonify

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "status": "error",
            "message": "Please enter a question."
        }), 400

    return jsonify({
        "status": "success",
        "message": (
            "Your question is: " + message +
            ". The chat endpoint is connected successfully. "
            "AI responses still need to be configured."
        )
    }), 200
