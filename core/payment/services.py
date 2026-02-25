# core/payment/services.py

from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.payment.models import Payment, PaymentMethod, PaymentStatus
from core.payment import selectors
from core.tenants.models import Tenant
from core.users.models import User
from core.wallet.services import debit_wallet, credit_wallet
from core.wallet.selectors import get_wallet


@transaction.atomic
def create_payment(*, tenant: Tenant, user: User, method_code: str, amount: float, reference: str = "", description: str = "") -> Payment:
    method = selectors.get_payment_method_by_code(tenant=tenant, code=method_code)
    if not method:
        raise ValidationError(f"Payment method '{method_code}' not found or inactive.")

    payment = Payment.objects.create(
        tenant=tenant,
        user=user,
        method=method,
        amount=amount,
        status=PaymentStatus.PENDING,
        reference=reference,
        description=description
    )

    # jika metode wallet, langsung debit user wallet
    if method.code == "wallet":
        wallet = get_wallet(tenant=tenant, user=user)
        if not wallet:
            raise ValidationError("User wallet not found.")
        debit_wallet(tenant=tenant, wallet=wallet, amount=amount, transaction_type="payment", reference=f"Payment:{payment.id}", description=description)
        payment.status = PaymentStatus.SUCCESS
        payment.save(update_fields=["status", "updated_at"])

    return payment


@transaction.atomic
def update_payment_status(*, payment: Payment, new_status: str):
    allowed = [PaymentStatus.PENDING, PaymentStatus.SUCCESS, PaymentStatus.FAILED, PaymentStatus.CANCELLED]
    if new_status not in allowed:
        raise ValidationError("Invalid payment status.")
    payment.status = new_status
    payment.save(update_fields=["status", "updated_at"])