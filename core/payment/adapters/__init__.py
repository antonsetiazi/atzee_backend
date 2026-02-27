# core/payment/adapters/__init__.py

from core.payment.models import PaymentGatewayType
from core.payment.adapters.wallet import WalletGateway
from core.payment.adapters.midtrans import MidtransGateway
from core.payment.adapters.xendit import XenditGateway


def get_gateway(gateway_type: str):
    if gateway_type == PaymentGatewayType.WALLET:
        return WalletGateway()

    if gateway_type == PaymentGatewayType.MIDTRANS:
        return MidtransGateway()

    if gateway_type == PaymentGatewayType.XENDIT:
        return XenditGateway()

    raise ValueError(f"Unsupported gateway: {gateway_type}")