import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WooCommerceService:

    def __init__(self):
        self.base_url = os.getenv("WOOCOMMERCE_URL", "").rstrip("/")
        self.consumer_key = os.getenv("WOOCOMMERCE_CONSUMER_KEY")
        self.consumer_secret = os.getenv("WOOCOMMERCE_CONSUMER_SECRET")

    def get_products(self):
        url = f"{self.base_url}/wp-json/wc/v3/products"

        response = requests.get(
            url,
            auth=(self.consumer_key, self.consumer_secret),
            params={"per_page": 100},
            timeout=30
        )

        print("WooCommerce status:", response.status_code)
        print("WooCommerce content-type:", response.headers.get("Content-Type"))
        print("WooCommerce response:", response.text[:500])

        response.raise_for_status()

        try:
            return response.json()
        except ValueError:
            raise Exception(
                f"WooCommerce did not return JSON. Response: {response.text[:500]}"
            )