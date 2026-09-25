import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WooCommerceService:
    def __init__(self):
        self.base_url = os.getenv("WOOCOMMERCE_URL", "").rstrip("/")

    def get_products(self):
        url = f"{self.base_url}/wp-json/wc/store/v1/products"

        params = {
            "per_page": 100
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }

        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=30
            )

            print("WooCommerce Store API URL:", url)
            print("WooCommerce status:", response.status_code)
            print(
                "WooCommerce content-type:",
                response.headers.get("Content-Type")
            )
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
            raise Exception(
                f"WooCommerce connection error: {e}"
            )