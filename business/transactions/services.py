from typing import List
from decimal import Decimal

from django.db import transaction
from django.core.exceptions import ValidationError

from core.tenants.models import Tenant
from core.users.models import User

from business.transactions.models.transaction import Transaction
from business.transactions.models.transaction_item import TransactionItem
from business.transactions.models.enums import (
    TransactionStatus,
    TransactionType
)
from business.transactions import selectors


@transaction.atomic
def create_transaction(
    *,
    tenant: Tenant,
    created_by: User,
    reference: str,
    transaction_type: str,
    transaction_date,
    customer=None,
    partner=None,
    notes: str | None = None,
) -> Transaction:
    """
    Create new transaction in DRAFT state.
    """

    if transaction_type == TransactionType.SALES and not customer:
        raise ValidationError("Sales transaction requires customer.")
    
    if transaction_type == TransactionType.PURCHASE and not partner:
        raise ValidationError("Purchase transaction requires partner.")
    
    trx = Transaction.objects.create(
        tenant=tenant,
        reference=reference,
        transaction_type=transaction_type,
        transaction_date=transaction_date,
        customer=customer,
        partner=partner,
        notes=notes,
        status=TransactionStatus.DRAFT,
        created_by=created_by,
    )

    return trx


@transaction.atomic
def add_transaction_item(
    *,
    tenant: Tenant,
    transaction_id: int,
    product,
    quantity: Decimal,
    unit_price: Decimal,
    created_by: User,
    notes: str | None = None,
) -> TransactionItem:
    """
    Add item to draft transaction.
    """

    trx = selectors.get_transaction_by_id(
        tenant=tenant,
        transaction_id=transaction_id
    )

    if not trx:
        raise ValidationError("Transaction not found.")

    if trx.status != TransactionStatus.DRAFT:
        raise ValidationError("Only draft transaction can be modified.")

    total_price = quantity * unit_price

    item = TransactionItem.objects.create(
        tenant=tenant,
        transaction=trx,
        product=product,
        quantity=quantity,
        unit_price=unit_price,
        total_price=total_price,
        notes=notes,
        created_by=created_by,
    )

    return item


@transaction.atomic
def remove_transaction_item(
    *,
    tenant: Tenant,
    transaction_id: int,
    item_id: int,
    deleted_by: User,
) -> None:
    """
    Remove item from draft transaction.
    """

    trx = selectors.get_transaction_by_id(
        tenant=tenant,
        transaction_id=transaction_id
    )

    if not trx:
        raise ValidationError("Transaction not found.")

    if trx.status != TransactionStatus.DRAFT:
        raise ValidationError("Only draft transaction can be modified.")

    try:
        item = trx.items.get(id=item_id)
    except TransactionItem.DoesNotExist:
        raise ValidationError("Transaction item not found.")

    item.delete()


@transaction.atomic
def confirm_transaction(
    *,
    tenant: Tenant,
    transaction_id: int,
    confirmed_by: User,
) -> Transaction:
    """
    Confirm transaction (lock data).
    """

    trx = selectors.get_transaction_by_id(
        tenant=tenant,
        transaction_id=transaction_id
    )

    if not trx:
        raise ValidationError("Transaction not found.")

    if trx.status != TransactionStatus.DRAFT:
        raise ValidationError("Only draft transaction can be confirmed.")

    if not trx.items.exists():
        raise ValidationError("Transaction must have at least one item.")

    # Domain hook points (future)
    # - validate stock availability
    # - reserve stock
    # - prepare accounting journal
    # - generate document snapshot

    trx.status = TransactionStatus.CONFIRMED
    trx.updated_by = confirmed_by
    trx.save(update_fields=[
        "status",
        "updated_by",
        "updated_at",
    ])

    return trx


@transaction.atomic
def cancel_transaction(
    *,
    tenant: Tenant,
    transaction_id: int,
    cancelled_by: User,
    reason: str | None = None,
) -> Transaction:
    """
    Cancel transaction.
    """

    trx = selectors.get_transaction_by_id(
        tenant=tenant,
        transaction_id=transaction_id
    )

    if not trx:
        raise ValidationError("Transaction not found.")

    if trx.status == TransactionStatus.COMPLETED:
        raise ValidationError("Completed transaction cannot be cancelled.")

    trx.status = TransactionStatus.CANCELLED
    trx.notes = reason or trx.notes
    trx.updated_by = cancelled_by
    trx.save(update_fields=[
        "status",
        "notes",
        "updated_by",
        "updated_at",
    ])

    return trx
