from typing import Optional
from django.db.models import QuerySet, Q

from business.customers.models import Customer
from core.tenants.models import Tenant


def get_customer_queryset(*, tenant: Tenant) -> QuerySet[Customer]:
    """
    Base queryset for customer (tenant scoped).
    """
    return Customer.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_customers(*, tenant: Tenant) -> QuerySet[Customer]:
    """
    Get all customers for a tenant.
    """
    return (
        get_customer_queryset(tenant=tenant)
        .order_by("name")
    )


def get_customer_by_id(*, tenant: Tenant, customer_id: int) -> Optional[Customer]:
    """
    Get single customer by ID.
    """
    try:
        return get_customer_queryset(tenant=tenant).get(id=customer_id)
    except Customer.DoesNotExist:
        return None
    

def search_customers(*, tenant: Tenant, keyword: str) -> QuerySet[Customer]: 
    """
    Search customer by name, phone, or email.
    """
    return (
        get_customer_queryset(tenant=tenant)
        .filter(
            Q(name__icontains=keyword)
            | Q(phone__icontains=keyword)
            | Q(email__icontains=keyword)
        )
        .order_by("name")
    )


def customer_exists(*, tenant: Tenant, customer_id: int) -> bool:
    return get_customer_queryset(tenant=tenant).filter(
        id=customer_id
    ).exists()