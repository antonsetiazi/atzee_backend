# core/payment/adapters/base.py

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class GatewayResult:
    external_id: str | None
    client_payload: Dict[str, Any] | None
    raw_response: Dict[str, Any] | None


class BasePaymentGateway:

    def create_transaction(self, *, payment) -> GatewayResult:
        raise NotImplementedError

    def handle_webhook(self, payload: dict) -> GatewayResult:
        raise NotImplementedError