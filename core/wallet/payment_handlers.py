# core/wallet/payment_handlers.py

from decimal import Decimal
from core.wallet import services as wallet_services
from core.wallet import selectors as wallet_selectors


def handle_wallet_topup(payment):
    tenant = payment.tenant

    # 🔥 reference_id = user.id
    user_id = payment.reference_id

    wallet = wallet_selectors.get_wallet_by_user_id(
        tenant=tenant,
        user_id=user_id
    )

    amount = Decimal(payment.amount)

    wallet_services.topup_wallet(
        tenant=tenant,
        wallet=wallet,
        amount=amount,
        idempotency_key=f"topup-{payment.external_reference}",
        description="Topup via Midtrans"
    )