# business/payment_gateway/providers/xendit.py

import requests
from django.conf import settings

from business.payment_gateway.providers.base import BasePaymentProvider


class XenditProvider(BasePaymentProvider):

    def _get_base_url(self):
        return "https://api.xendit.co"

    def create_payment(self, payment):
        url = f"{self._get_base_url()}/v2/invoices"

        headers = {
            "Content-Type": "application/json",
        }

        auth = (self.config.api_key, "")

        external_id = f"{payment.reference_type}-{payment.reference_id}-{payment.id}"

        payload = {
            "external_id": external_id,
            "amount": float(payment.amount),
            "description": f"Payment for {payment.reference_type}",
        }

        response = requests.post(url, json=payload, headers=headers, auth=auth)
        data = response.json()

        return {
            "external_id": data.get("id"),
            "external_reference": data.get("external_id"),
            "payment_url": data.get("invoice_url"),
            "payment_token": None,
            "raw": data,
        }

    def parse_webhook(self, payload: dict) -> dict:
        """
        Normalize Xendit webhook
        """

        status_map = {
            "PAID": "SUCCESS",
            "PENDING": "PENDING",
            "EXPIRED": "EXPIRED",
            "FAILED": "FAILED",
        }

        return {
            "external_id": payload.get("id"),
            "external_reference": payload.get("external_id"),
            "status": status_map.get(payload.get("status"), "PENDING"),
            "raw": payload,
        }