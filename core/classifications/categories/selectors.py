# core/classifications/categories/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.classifications.categories.models import Category
from core.tenants.models import Tenant


def get_category_queryset(*, tenant: Tenant) -> QuerySet[Category]:
    return Category.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )


def get_categories(
    *,
    tenant: Tenant,
    scope: Optional[str] = None,
    parent_id: Optional[int] = None,
) -> QuerySet[Category]:
    qs = get_category_queryset(tenant=tenant)

    if scope:
        qs = qs.filter(scope=scope)

    if parent_id is not None:
        qs = qs.filter(parent_id=parent_id)

    return qs.filter(is_active=True)


def get_category_by_id(
    *,
    tenant: Tenant,
    category_id: int,
) -> Optional[Category]:
    try:
        return get_category_queryset(
            tenant=tenant
        ).get(id=category_id)
    except Category.DoesNotExist:
        return None
