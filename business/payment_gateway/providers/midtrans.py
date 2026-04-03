# business/payment_gateway/providers/midtrans.py

import requests
import base64
import hashlib

from business.payment_gateway.providers.base import BasePaymentProvider


class MidtransProvider(BasePaymentProvider):

    # =========================
    # 🔧 CONFIG & UTIL
    # =========================

    def _get_base_url(self):
        if self.config and self.config.environment == "production":
            return "https://app.midtrans.com"
        return "https://app.sandbox.midtrans.com"

    def _get_server_key(self):
        """
        Server key WAJIB dari database (PaymentGatewayConfig)
        """
        if not self.config or not self.config.api_key:
            raise Exception("Midtrans server key not configured")

        return self.config.api_key.strip()

    def _get_headers(self):
        server_key = self._get_server_key()

        encoded = base64.b64encode(f"{server_key}:".encode()).decode()

        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Basic {encoded}",
        }

    # =========================
    # 💳 CREATE PAYMENT
    # =========================

    def create_payment(self, payment):
        url = f"{self._get_base_url()}/snap/v1/transactions"

        order_id = f"{payment.reference_type}-{payment.reference_id}-{payment.id}"

        payload = {
            "transaction_details": {
                "order_id": order_id,
                "gross_amount": int(float(payment.amount)),
            },
            "customer_details": {
                "first_name": "Customer",
            },
            "enabled_payments": [
                "gopay",
                "shopeepay",
                "bank_transfer",
                "qris",
            ],
        }

        headers = self._get_headers()

        response = requests.post(url, json=payload, headers=headers)

        try:
            data = response.json()
        except Exception:
            raise Exception(f"Midtrans invalid response: {response.text}")

        if response.status_code not in [200, 201]:
            raise Exception(f"Midtrans error: {data}")

        return {
            "external_id": data.get("token"),
            "external_reference": order_id,
            "payment_url": data.get("redirect_url"),
            "payment_token": data.get("token"),
            "raw": data,
        }

    # =========================
    # 🔐 SIGNATURE VALIDATION
    # =========================

    def validate_signature(self, payload: dict) -> bool:
        """
        Validate Midtrans signature

        Formula:
        SHA512(order_id + status_code + gross_amount + server_key)
        """

        try:
            order_id = payload.get("order_id", "")
            status_code = payload.get("status_code", "")
            gross_amount = payload.get("gross_amount", "")
            signature_key = payload.get("signature_key", "")

            server_key = self._get_server_key()

            raw_string = f"{order_id}{status_code}{gross_amount}{server_key}"

            expected_signature = hashlib.sha512(
                raw_string.encode("utf-8")
            ).hexdigest()

            return expected_signature == signature_key

        except Exception:
            return False

    # =========================
    # 🔄 PARSE WEBHOOK
    # =========================

    def parse_webhook(self, payload: dict) -> dict:
        """
        Normalize Midtrans webhook → internal format
        """

        status_map = {
            "capture": "SUCCESS",
            "settlement": "SUCCESS",
            "pending": "PENDING",
            "deny": "FAILED",
            "cancel": "FAILED",
            "expire": "EXPIRED",
        }

        transaction_status = payload.get("transaction_status")

        return {
            "external_id": payload.get("transaction_id"),
            "external_reference": payload.get("order_id"),
            "status": status_map.get(transaction_status, "PENDING"),
            "payment_type": payload.get("payment_type"),
            "fraud_status": payload.get("fraud_status"),
            "gross_amount": payload.get("gross_amount"),
            "raw": payload,
        }