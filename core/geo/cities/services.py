# core/geo/cities/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.geo.cities.models import City
from core.geo.cities import selectors
from core.geo.countries.selectors import get_country_by_id
from core.geo.regions.selectors import get_region_by_id
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_city_uniqueness(
    *,
    region_id: int,
    code: str,
    exclude_city_id: Optional[int] = None,
):
    qs = selectors.get_city_queryset().filter(
        region_id=region_id,
        code=code,
    )

    if exclude_city_id:
        qs = qs.exclude(id=exclude_city_id)

    if qs.exists():
        raise ValidationError(
            "City with this code already exists in this region."
        )


@transaction.atomic
def create_city(
    *,
    created_by: User,
    country_id: int,
    region_id: int,
    code: str,
    name: str,
    center_latitude: Optional[float] = None,
    center_longitude: Optional[float] = None,
) -> City:

    country = get_country_by_id(country_id=country_id)
    if not country:
        raise ValidationError("Country not found.")

    region = get_region_by_id(region_id=region_id)
    if not region:
        raise ValidationError("Region not found.")

    code = _normalize(code).upper()
    name = _normalize(name)

    _validate_city_uniqueness(
        region_id=region.id,
        code=code,
    )

    return City.objects.create(
        country=country,
        region=region,
        code=code,
        name=name,
        center_latitude=center_latitude,
        center_longitude=center_longitude,
        created_by=created_by,
    )