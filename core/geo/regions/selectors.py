# core/geo/regions/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.geo.regions.models import Region
from core.geo.countries.models import Country
from core.tenants.models import Tenant


def get_region_queryset(*, tenant: Tenant) -> QuerySet[Region]:
    return Region.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True,
    ).select_related("country")


def get_regions(
    *,
    tenant: Tenant,
    country: Optional[Country] = None,
) -> QuerySet[Region]:
    qs = get_region_queryset(tenant=tenant)
    if country:
        qs = qs.filter(country=country)
    return qs


def get_region_by_id(
    *,
    tenant: Tenant,
    region_id: int,
) -> Optional[Region]:
    try:
        return get_region_queryset(
            tenant=tenant
        ).get(id=region_id)
    except Region.DoesNotExist:
        return None
