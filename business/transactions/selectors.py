from typing import Optional
from django.db.models import QuerySet, Prefetch

from core.tenants.models import Tenant
from business.transactions.models.transaction import Transaction
from business.transactions.models.transaction_item import TransactionItem
from business.transactions.models.enums import (
    TransactionType,
    TransactionStatus
)


def get_transaction_queryset(*, tenant: Tenant) -> QuerySet[Transaction]:
    """
    Base queryset for transaction (tenant scoped).
    """
    return (
        Transaction.objects
        .filter(
            tenant=tenant,
            is_deleted=False,
        )
        .select_related(
            "customer", "partner"
        )
        .prefetch_related(
            Prefetch(
                "items",
                queryset=TransactionItem.objects.filter(
                    is_deleted=False
                ).select_related("product")
            )
        )
    )


def get_transactions(*, tenant: Tenant) -> QuerySet[Transaction]:
    """
    Get all transactions for tenant.
    """
    return (
        get_transaction_queryset(tenant=tenant)
        .order_by("-transaction_date", "-id")
    )


def get_transaction_by_id(
        *,
        tenant: Tenant,
        transaction_id: int,
) -> Optional[Transaction]:
    """
    Get single transaction by ID.
    """
    try:
        return get_transaction_queryset(tenant=tenant).get(id=transaction_id)
    except Transaction.DoesNotExist:
        return None
    

def get_transactions_by_type(
        *, 
        tenant: Tenant,
        transaction_type: TransactionType,
) -> QuerySet[Transaction]:
    """
    Get transactions by type (sales, purchase, etc).
    """
    return (
        get_transaction_queryset(tenant=tenant)
        .filter(transaction_type=transaction_type)
        .order_by("-transaction_date")
    )
    

def get_transactions_by_status(
        *, 
        tenant: Tenant,
        status: TransactionStatus,
) -> QuerySet[Transaction]:
    """
    Get transactions by status.
    """
    return (
        get_transaction_queryset(tenant=tenant)
        .filter(status=status)
        .order_by("-transaction_date")
    )


def search_transactions(
    *,
    tenant: Tenant,
    keyword: str,
) -> QuerySet[Transaction]:
    """
    Search transaction by reference.
    """
    return (
        get_transaction_queryset(tenant=tenant)
        .filter(reference__icontains=keyword)
        .order_by("-transaction_date")
    )


def transaction_exists(
    *,
    tenant: Tenant,
    transaction_id: int,
) -> bool:
    """
    Check transaction existence.
    """
    return (
        get_transaction_queryset(tenant=tenant)
        .filter(id=transaction_id)
        .exists()
    )
