# core/geo/villages/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.geo.villages.models import Village
from core.geo.villages import selectors
from core.geo.countries.selectors import get_country_by_id
from core.geo.regions.selectors import get_region_by_id
from core.geo.cities.selectors import get_city_by_id
from core.geo.districts.selectors import get_district_by_id
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_uniqueness(
    *,
    district_id: int,
    code: str,
    exclude_village_id: Optional[int] = None,
):
    qs = selectors.get_village_queryset().filter(
        district_id=district_id,
        code=code,
    )

    if exclude_village_id:
        qs = qs.exclude(id=exclude_village_id)

    if qs.exists():
        raise ValidationError(
            "Village with this code already exists in this district."
        )


@transaction.atomic
def create_village(
    *,
    created_by: User,
    country_id: int,
    region_id: int,
    city_id: int,
    district_id: int,
    code: str,
    name: str,
    center_latitude: Optional[float] = None,
    center_longitude: Optional[float] = None,
) -> Village:

    country = get_country_by_id(country_id=country_id)
    region = get_region_by_id(region_id=region_id)
    city = get_city_by_id(city_id=city_id)
    district = get_district_by_id(district_id=district_id)

    if not country:
        raise ValidationError("Country not found.")
    if not region:
        raise ValidationError("Region not found.")
    if not city:
        raise ValidationError("City not found.")
    if not district:
        raise ValidationError("District not found.")

    if district.city_id != city.id:
        raise ValidationError("District does not belong to selected city.")

    if city.region_id != region.id:
        raise ValidationError("City does not belong to selected region.")

    if region.country_id != country.id:
        raise ValidationError("Region does not belong to selected country.")

    code = _normalize(code).upper()
    name = _normalize(name)

    _validate_uniqueness(
        district_id=district.id,
        code=code,
    )

    return Village.objects.create(
        country=country,
        region=region,
        city=city,
        district=district,
        code=code,
        name=name,
        center_latitude=center_latitude,
        center_longitude=center_longitude,
        created_by=created_by,
    )