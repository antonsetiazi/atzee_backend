# core/payment/services.py

from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.payment.models import Payment, PaymentMethod, PaymentStatus
from core.payment.models import PaymentGatewayType
from core.payment import selectors
from core.tenants.models import Tenant
from core.users.models import User
from core.wallet.services import debit_wallet, credit_wallet
from core.wallet.selectors import get_wallet
from core.payment.adapters import get_gateway


FINAL_STATUSES = {
    PaymentStatus.SUCCESS,
    PaymentStatus.FAILED,
    PaymentStatus.CANCELLED,
}

ALLOWED_TRANSITIONS = {
    PaymentStatus.DRAFT: {PaymentStatus.PENDING},
    PaymentStatus.PENDING: {
        PaymentStatus.SUCCESS,
        PaymentStatus.FAILED,
        PaymentStatus.CANCELLED,
    },
}


def can_transition(current_status: str, new_status: str) -> bool:
    # Final state cannot change
    if current_status in FINAL_STATUSES:
        return False

    allowed = ALLOWED_TRANSITIONS.get(current_status, set())
    return new_status in allowed


@transaction.atomic
def create_payment(*, tenant: Tenant, user: User, method_code: str, amount: float, reference: str = "", description: str = "") -> Payment:
    method = selectors.get_payment_method_by_code(
        tenant=tenant, 
        code=method_code
    )

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

    gateway = get_gateway(method.gateway)

    result = gateway.create_transaction(payment=payment)

    payment.external_id = result.external_id
    payment.gateway_response = result.raw_response
    payment.client_payload = result.client_payload
    payment.save(update_fields=[
        "external_id",
        "gateway_response",
        "client_payload",
        "updated_at",
    ])

    return payment


@transaction.atomic
def update_payment_status(*, payment: Payment, new_status: str):
    
    if not can_transition(payment.status, new_status):
        raise ValidationError(
            f"Invalid status transition from {payment.status} to {new_status}"
        )
    
    payment.status = new_status
    payment.save(update_fields=["status", "updated_at"])