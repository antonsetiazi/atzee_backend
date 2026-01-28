from typing import Optional
from django.db.models import QuerySet, Q

from business.products.models import Product
from core.tenants.models import Tenant


def get_product_queryset(*, tenant: Tenant) -> QuerySet[Product]:
    """
    Base queryset for product (tenant scoped).
    """
    return Product.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_products(
        *, 
        tenant: Tenant,
        only_active: bool = True
) -> QuerySet[Product]:
    """
    Get all products for a tenant.
    """

    qs = get_product_queryset(tenant=tenant)

    if only_active:
        qs = qs.filter(is_active=True)

    return qs.order_by("name")


def get_product_by_id(
        *, 
        tenant: Tenant, 
        product_id: int
) -> Optional[Product]:
    """
    Get single product by ID.
    """
    try:
        return get_product_queryset(tenant=tenant).get(id=product_id)
    except Product.DoesNotExist:
        return None
    

def search_products(
        *, 
        tenant: Tenant, 
        keyword: str
) -> QuerySet[Product]: 
    """
    Search product by name or code.
    """
    return (
        get_product_queryset(tenant=tenant)
        .filter(
            Q(name__icontains=keyword)
            | Q(code__icontains=keyword)
        )
        .order_by("name")
    )


def product_exists(
        *, 
        tenant: Tenant, 
        product_id: int
) -> bool:
    return get_product_queryset(tenant=tenant).filter(
        id=product_id
    ).exists()