from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError

from business.payments.models import Payment
from business.payments import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _validate_amount(amount: Decimal) -> None:
    if amount <= 0:
        raise ValidationError("Payment amount must be greater than zero.")
    

@transaction.atomic
def create_payment(
    *,
    tenant: Tenant,
    created_by: User,
    direction: str,
    amount: Decimal,
    payment_date,
    method: str,
    currency: str = "IDR",
    reference_number: str | None = None,
    document_id: int | None = None,
    notes: str | None = None
) -> Payment:
    """
    Create new payment (draft by default).
    """

    _validate_amount(amount)

    payment = Payment.objects.create(
        tenant=tenant,
        direction=direction,
        amount=amount,
        currency=currency,
        method=method,
        payment_date=payment_date,
        reference_number=reference_number,
        document_id=document_id,
        notes=notes,
        status=Payment.STATUS_DRAFT,
        created_by=created_by
    )

    return payment


@transaction.atomic
def post_payment(
    *,
    tenant: Tenant,
    payment_id: int,
    posted_by: User
) -> Payment:
    """
    Finalize payment (immutable event).
    """

    payment = selectors.get_payment_by_id(
        tenant=tenant,
        payment_id=payment_id
    )

    if not payment:
        raise ValidationError("Payment not found.")
    
    if payment.status != Payment.STATUS_DRAFT:
        raise ValidationError("Only draft payment can bbe posted.")
    
    payment.status = Payment.STATUS_POSTED
    payment.updated_by = posted_by
    payment.save(update_fields=[
        "status",
        "updated_by",
        "updated_at"
    ])

    return payment


@transaction.atomic
def void_payment(
    *,
    tenant: Tenant,
    payment_id: int,
    voided_by: User,
    reason: str | None = None
) -> Payment:
    """
    Void payment (no deletion).
    """

    payment = selectors.get_payment_by_id(
        tenant=tenant,
        payment_id=payment_id
    )

    if not payment:
        raise ValidationError("Payment not found.")
    
    if payment.status == Payment.STATUS_VOID:
        raise ValidationError("Payment already voided.")
    
    payment.status = Payment.STATUS_VOID
    payment.notes = reason or payment.notes
    payment.updated_by = voided_by
    payment.save(update_fields=[
        "status",
        "notes",
        "updated_by",
        "updated_at"
    ])

    return payment