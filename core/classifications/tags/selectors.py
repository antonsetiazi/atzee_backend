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


def get_tags_by_ids(*, tenant: Tenant, ids: list[int]) -> QuerySet[Tag]:
    return get_tag_queryset(tenant=tenant).filter(id__in=ids)


def search_tags(*, tenant: Tenant, keyword: str) -> QuerySet[Tag]:
    return get_tags(tenant=tenant).filter(name__icontains=keyword)
