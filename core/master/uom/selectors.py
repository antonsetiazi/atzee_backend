# core/master/uom/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.master.uom.models import UOM, UOMCategory
from core.tenants.models import Tenant


def get_uom_queryset(*, tenant: Tenant) -> QuerySet[UOM]:
    return UOM.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True
    )


def get_uoms(*, tenant: Tenant) -> QuerySet[UOM]:
    return get_uom_queryset(tenant=tenant).select_related(
        "category"
    ).order_by("name")


def get_uom_by_id(
    *, tenant: Tenant, uom_id: int
) -> Optional[UOM]:
    try:
        return get_uom_queryset(tenant=tenant).get(id=uom_id)
    except UOM.DoesNotExist:
        return None


def get_categories(*, tenant: Tenant) -> QuerySet[UOMCategory]:
    return UOMCategory.objects.filter(
        tenant=tenant,
        is_deleted=False
    ).order_by("name")


def get_category_by_id(*, tenant: Tenant, category_id: int) -> QuerySet[UOMCategory]:
    return UOMCategory.objects.filter(
        tenant=tenant,
        is_deleted=False
    ).get(id=category_id)
