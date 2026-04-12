# core/geo/villages/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.geo.villages.models import Village


def get_village_queryset() -> QuerySet[Village]:
    return Village.objects.filter(
        is_deleted=False,
        is_active=True,
    ).select_related(
        "country",
        "region",
        "city",
        "district",
    )


def get_villages(
    *,
    country_id: Optional[int] = None,
    region_id: Optional[int] = None,
    city_id: Optional[int] = None,
    district_id: Optional[int] = None,
) -> QuerySet[Village]:
    qs = get_village_queryset()

    if country_id:
        qs = qs.filter(country_id=country_id)

    if region_id:
        qs = qs.filter(region_id=region_id)

    if city_id:
        qs = qs.filter(city_id=city_id)

    if district_id:
        qs = qs.filter(district_id=district_id)

    return qs


def get_village_by_id(village_id: int):
    try:
        return get_village_queryset().get(id=village_id)
    except Village.DoesNotExist:
        return None