# core/payment/adapters/xendit.py

from core.payment.adapters.base import BasePaymentGateway, GatewayResult


class XenditGateway(BasePaymentGateway):

    def create_transaction(self, *, payment) -> GatewayResult:
        # TODO
        return GatewayResult(
            external_id=None,
            client_payload=None,
            raw_response=None,
        )

    def handle_webhook(self, payload: dict) -> GatewayResult:
        # TODO
        return GatewayResult(
            external_id=None,
            client_payload=None,
            raw_response=payload,
        )