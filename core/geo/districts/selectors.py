# core/geo/districts/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.geo.districts.models import District


def get_district_queryset() -> QuerySet[District]:
    return District.objects.filter(
        is_deleted=False,
        is_active=True,
    ).select_related(
        "country",
        "region",
        "city",
    )


def get_districts(
    *,
    country_id: Optional[int] = None,
    region_id: Optional[int] = None,
    city_id: Optional[int] = None,
) -> QuerySet[District]:
    qs = get_district_queryset()

    if country_id:
        qs = qs.filter(country_id=country_id)

    if region_id:
        qs = qs.filter(region_id=region_id)

    if city_id:
        qs = qs.filter(city_id=city_id)

    return qs


def get_district_by_id(district_id: int):
    try:
        return get_district_queryset().get(id=district_id)
    except District.DoesNotExist:
        return None