# business/products/selectors.py

from typing import Optional
from django.db.models import QuerySet, Q

from business.products.models import Product, PartnerOffering
from core.tenants.models import Tenant


def get_product_queryset(*, tenant: Tenant) -> QuerySet[Product]:
    return Product.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_products(
        *, 
        tenant: Tenant,
        only_active: bool = True,
        product_type: Optional[str] = None
) -> QuerySet[Product]:
    qs = get_product_queryset(tenant=tenant)

    if only_active:
        qs = qs.filter(is_active=True)

    if product_type:
        qs = qs.filter(product_type=product_type)

    return qs.order_by("name")


def get_product_by_id(
        *, 
        tenant: Tenant, 
        product_id: int
) -> Optional[Product]:
    return get_product_queryset(tenant=tenant).filter(id=product_id).first()
    

def search_products(
        *, 
        tenant: Tenant, 
        keyword: str
) -> QuerySet[Product]: 
    return (
        get_product_queryset(tenant=tenant)
        .filter(
            Q(name__icontains=keyword) | 
            Q(code__icontains=keyword)
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


# 🔥 CLEAN: offering instead of service
def get_partner_offerings(
    *,
    tenant: Tenant,
    partner_id: int,
    only_active: bool = True,
    product_type: Optional[str] = None
) -> QuerySet[PartnerOffering]:

    qs = (
        PartnerOffering.objects
        .filter(
            tenant=tenant,
            partner_id=partner_id,
            product__is_deleted=False,
            product__is_active=True,
        )
        .select_related("product")
    )

    if only_active:
        qs = qs.filter(is_active=True)

    if product_type:
        qs = qs.filter(product__product_type=product_type)

    return qs.order_by("product__name")