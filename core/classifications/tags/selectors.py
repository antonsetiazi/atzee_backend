# core/classifications/tags/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.classifications.tags.models import Tag
from core.tenants.models import Tenant


def get_tag_queryset(*, tenant: Tenant) -> QuerySet[Tag]:
    return Tag.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )


def get_tags(*, tenant: Tenant) -> QuerySet[Tag]:
    return get_tag_queryset(tenant=tenant).filter(is_active=True)


def get_tag_by_id(*, tenant: Tenant, tag_id: int) -> Optional[Tag]:
    try:
        return get_tag_queryset(tenant=tenant).get(id=tag_id)
    except Tag.DoesNotExist:
        return None
