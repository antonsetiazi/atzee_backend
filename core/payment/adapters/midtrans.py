# core/payment/adapters/midtrans.py

import midtransclient
from django.conf import settings

from core.payment.adapters.base import BasePaymentGateway, GatewayResult
from core.payment.models import PaymentStatus


class MidtransGateway(BasePaymentGateway):

    def __init__(self):
        self.snap = midtransclient.Snap(
            is_production=settings.MIDTRANS_IS_PRODUCTION,
            server_key=settings.MIDTRANS_SERVER_KEY,
            client_key=settings.MIDTRANS_CLIENT_KEY,
        )

    def create_transaction(self, *, payment) -> GatewayResult:

        transaction_data = {
            "transaction_details": {
                "order_id": f"ATZ-{payment.id}",
                "gross_amount": float(payment.amount),
            },
            "customer_details": {
                "first_name": payment.user.full_name or payment.user.username,
                "email": payment.user.email,
            },
        }

        response = self.snap.create_transaction(transaction_data)

        snap_token = response.get("token")
        redirect_url = response.get("redirect_url")

        return GatewayResult(
            external_id=f"ATZ-{payment.id}",
            client_payload={
                "snap_token": snap_token,
                "redirect_url": redirect_url,
            },
            raw_response=response,
        )

    def handle_webhook(self, payload: dict) -> GatewayResult:
        transaction_status = payload.get("transaction_status")
        order_id = payload.get("order_id")

        return GatewayResult(
            external_id=order_id,
            client_payload=None,
            raw_response=payload,
        )