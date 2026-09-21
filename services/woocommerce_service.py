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

        params = {
            "consumer_key": self.consumer_key,
            "consumer_secret": self.consumer_secret,
            "per_page": 100
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/153.0.0.0 Safari/537.36",
            "Accept": "application/json"
        }

        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=30
            )

            print("WooCommerce URL:", url)
            print("WooCommerce status:", response.status_code)
            print("WooCommerce content-type:", response.headers.get("Content-Type"))
            print("WooCommerce response:", response.text[:500])

            response.raise_for_status()

            try:
                return response.json()
            except ValueError:
                raise Exception(
                    f"WooCommerce did not return JSON. "
                    f"Response: {response.text[:500]}"
                )

        except requests.exceptions.RequestException as e:
            print("WooCommerce connection error:", repr(e))
            raise Exception(f"WooCommerce connection error: {e}")