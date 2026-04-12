# core/geo/regions/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.geo.regions.models import Region
from core.geo.countries.models import Country


def get_region_queryset() -> QuerySet[Region]:
    return Region.objects.filter(
        is_deleted=False,
        is_active=True,
    ).select_related("country")


def get_regions(
    *,
    country_id: Optional[int] = None,
) -> QuerySet[Region]:
    qs = get_region_queryset()
    if country_id:
        qs = qs.filter(country_id=country_id)

    return qs


def get_region_by_id(
    *,
    region_id: int,
) -> Optional[Region]:
    try:
        return get_region_queryset(
        ).get(id=region_id)
    except Region.DoesNotExist:
        return None
