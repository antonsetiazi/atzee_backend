# core/geo/timezones/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.geo.timezones.models import Timezone
from core.tenants.models import Tenant


def get_timezone_queryset(*, tenant: Tenant) -> QuerySet[Timezone]:
    return Timezone.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )


def get_timezones(*, tenant: Tenant) -> QuerySet[Timezone]:
    return get_timezone_queryset(
        tenant=tenant
    ).filter(is_active=True)


def get_timezone_by_id(
    *,
    tenant: Tenant,
    timezone_id: int
) -> Optional[Timezone]:
    try:
        return get_timezone_queryset(
            tenant=tenant
        ).get(id=timezone_id)
    except Timezone.DoesNotExist:
        return None
