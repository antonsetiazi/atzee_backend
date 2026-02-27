# core/payment/adapters/wallet.py

from core.payment.adapters.base import BasePaymentGateway, GatewayResult
from core.wallet.selectors import get_wallet
from core.wallet.services import debit_wallet
from core.payment.models import PaymentStatus


class WalletGateway(BasePaymentGateway):

    def create_transaction(self, *, payment) -> GatewayResult:
        wallet = get_wallet(tenant=payment.tenant, user=payment.user)
        if not wallet:
            raise Exception("User wallet not found.")

        debit_wallet(
            tenant=payment.tenant,
            wallet=wallet,
            amount=payment.amount,
            transaction_type="payment",
            reference=f"Payment:{payment.id}",
            description=payment.description,
        )

        payment.status = PaymentStatus.SUCCESS
        payment.save(update_fields=["status", "updated_at"])

        return GatewayResult(
            external_id=None,
            client_payload=None,
            raw_response=None,
        )