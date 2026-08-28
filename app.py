from flask import Flask, jsonify
from flask_cors import CORS

from routes.products import products_bp


app = Flask(__name__)

CORS(app)

app.register_blueprint(products_bp)


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "E-commerce AI Backend is running!"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend is healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)