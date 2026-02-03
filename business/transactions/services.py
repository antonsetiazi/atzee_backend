# business/transactions/services.py

from typing import List
from decimal import Decimal

from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Max

from core.tenants.models import Tenant
from core.users.models import User

from business.transactions.models.transaction import Transaction
from business.transactions.models.transaction_item import TransactionItem
from business.transactions.models.enums import (
    TransactionStatus,
    TransactionType,
    TransactionSubType
)
from business.transactions import selectors

from core.workflows.engine import WorkflowEngine
from core.workflows.context import WorkflowContext

@transaction.atomic
def create_transaction(
    *,
    tenant: Tenant,
    created_by: User,
    reference: str,
    transaction_type: str,
    transaction_date,
    subtype: str | None = None,
    customer=None,
    partner=None,
    notes: str | None = None,
) -> Transaction:
    """
    Create new transaction in DRAFT state.
    """

    if transaction_type == TransactionType.SALES:
        if not customer:
            raise ValidationError("Sales transaction requires customer.")

        if subtype is None:
            subtype = TransactionSubType.DIRECT
    
    if transaction_type == TransactionType.PURCHASE and not partner:
        raise ValidationError("Purchase transaction requires partner.")
    
    trx = Transaction.objects.create(
        tenant=tenant,
        reference=reference,
        transaction_type=transaction_type,
        subtype=subtype,
        transaction_date=transaction_date,
        customer=customer,
        partner=partner,
        notes=notes,
        status=TransactionStatus.DRAFT,
        created_by=created_by,
    )

    return trx


@transaction.atomic
def update_transaction(
    *,
    tenant: Tenant,
    transaction_id: int,
    updated_by: User,
    transaction_date,
    notes: str | None = None,
) -> Transaction:
    """
    Update existing transaction.
    """

    transaction = selectors.get_transaction_by_id(
        tenant=tenant,
        transaction_id=transaction_id
    )
    
    if not transaction:
        raise ValidationError("Transaction not found.")
    
    if transaction_date is not None:
        transaction.transaction_date = transaction_date
        
    if notes is not None:
        transaction.notes = notes

    transaction.updated_by = updated_by
    transaction.save(update_fields=[
        "transaction_date",
        "notes",
        "updated_by",
        "updated_at"
    ])

    return transaction


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
def update_transaction_item(
    *,
    tenant: Tenant,
    transaction_id: int,
    item_id: int,
    updated_by: User,
    quantity: Decimal | None = None,
    unit_price: Decimal | None = None,
    notes: str | None = None,
) -> TransactionItem:
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

    if quantity is not None:
        item.quantity = quantity

    if unit_price is not None:
        item.unit_price = unit_price

    if quantity is not None or unit_price is not None:
        item.total_price = item.quantity * item.unit_price

    if notes is not None:
        item.notes = notes

    item.updated_by = updated_by
    item.save(update_fields=[
        "quantity",
        "unit_price",
        "total_price",
        "notes",
        "updated_by",
        "updated_at",
    ])

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

    context = WorkflowContext(
        tenant=tenant,
        user=confirmed_by,
        transaction=trx,
    )

    WorkflowEngine.run(
        event="transaction.confirmed",
        context=context,
    )

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


def generate_sales_reference(tenant):
    """
    Generate human-readable sales reference.
    Format:
        SLS-YYYYMM-XXXX
    Example:
        SLS-202602-0001
    """

    today = timezone.now()
    prefix = f"SLS-{today:%Y%m}"

    last_ref = (
        Transaction.objects
        .filter(
            tenant=tenant,
            reference__startswith=prefix,
        )
        .aggregate(max_ref=Max("reference"))
        .get("max_ref")
    )

    if not last_ref:
        next_number = 1
    else:
        next_number = int(last_ref.split("-")[-1]) + 1

    return f"{prefix}-{next_number:04d}"
