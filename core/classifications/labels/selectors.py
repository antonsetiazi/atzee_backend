# core/classifications/labels/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.classifications.labels.models import Label
from core.tenants.models import Tenant


def get_label_queryset(*, tenant: Tenant) -> QuerySet[Label]:
    return Label.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )


def get_labels(
    *,
    tenant: Tenant,
    scope: Optional[str] = None,
) -> QuerySet[Label]:
    qs = get_label_queryset(tenant=tenant)
    if scope:
        qs = qs.filter(scope=scope)
    return qs.filter(is_active=True)


def get_label_by_id(
    *,
    tenant: Tenant,
    label_id: int,
) -> Optional[Label]:
    try:
        return get_label_queryset(tenant=tenant).get(id=label_id)
    except Label.DoesNotExist:
        return None
