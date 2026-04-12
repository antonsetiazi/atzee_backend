# core/geo/districts/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.geo.districts.models import District
from core.geo.districts import selectors
from core.geo.countries.selectors import get_country_by_id
from core.geo.regions.selectors import get_region_by_id
from core.geo.cities.selectors import get_city_by_id
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_uniqueness(
    *,
    city_id: int,
    code: str,
    exclude_district_id: Optional[int] = None,
):
    qs = selectors.get_district_queryset().filter(
        city_id=city_id,
        code=code,
    )

    if exclude_district_id:
        qs = qs.exclude(id=exclude_district_id)

    if qs.exists():
        raise ValidationError(
            "District with this code already exists in this city."
        )


@transaction.atomic
def create_district(
    *,
    created_by: User,
    country_id: int,
    region_id: int,
    city_id: int,
    code: str,
    name: str,
    center_latitude: Optional[float] = None,
    center_longitude: Optional[float] = None,
) -> District:

    country = get_country_by_id(country_id=country_id)
    region = get_region_by_id(region_id=region_id)
    city = get_city_by_id(city_id=city_id)

    if not country:
        raise ValidationError("Country not found.")
    if not region:
        raise ValidationError("Region not found.")
    if not city:
        raise ValidationError("City not found.")

    if city.region_id != region.id:
        raise ValidationError(
            "City does not belong to selected region."
        )

    if region.country_id != country.id:
        raise ValidationError(
            "Region does not belong to selected country."
        )

    code = _normalize(code).upper()
    name = _normalize(name)

    _validate_uniqueness(
        city_id=city.id,
        code=code,
    )

    return District.objects.create(
        country=country,
        region=region,
        city=city,
        code=code,
        name=name,
        center_latitude=center_latitude,
        center_longitude=center_longitude,
        created_by=created_by,
    )