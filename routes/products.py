from flask import Blueprint, jsonify
from services.woocommerce_service import WooCommerceService


products_bp = Blueprint("products", __name__)

woocommerce = WooCommerceService()


@products_bp.route("/api/products", methods=["GET"])
def get_products():

    try:
        products = woocommerce.get_products()

        return jsonify({
            "status": "success",
            "count": len(products),
            "products": products
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500