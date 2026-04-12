# core/geo/cities/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.geo.cities.models import City


def get_city_queryset() -> QuerySet[City]:
    return City.objects.filter(
        is_deleted=False,
        is_active=True,
    ).select_related(
        "country",
        "region"
    )


def get_cities(
    *,
    country_id: Optional[int] = None,
    region_id: Optional[int] = None,
) -> QuerySet[City]:
    qs = get_city_queryset()

    if country_id:
        qs = qs.filter(country_id=country_id)

    if region_id:
        qs = qs.filter(region_id=region_id)

    return qs


def get_city_by_id(city_id: int) -> Optional[City]:
    try:
        return get_city_queryset().get(id=city_id)
    except City.DoesNotExist:
        return None