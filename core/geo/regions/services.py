# core/geo/regions/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.geo.regions.models import Region
from core.geo.regions import selectors
from core.geo.countries.selectors import get_country_by_id
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_region_uniqueness(
    *,
    country_id: int,
    code: str,
    exclude_region_id: Optional[int] = None,
) -> None:
    qs = selectors.get_region_queryset().filter(
        country_id=country_id,
        code=code,
    )

    if exclude_region_id:
        qs = qs.exclude(id=exclude_region_id)

    if qs.exists():
        raise ValidationError(
            "Region with this code already exists for this country."
        )


@transaction.atomic
def create_region(
    *,
    created_by: User,
    country_id: int,
    code: str,
    name: str,
) -> Region:

    country = get_country_by_id(
        country_id=country_id
    )

    if not country:
        raise ValidationError("Country not found.")

    code = _normalize(code).upper()
    name = _normalize(name)

    _validate_region_uniqueness(
        country_id=country.id,
        code=code,
    )

    return Region.objects.create(
        country=country,
        code=code,
        name=name,
        created_by=created_by,
    )


@transaction.atomic
def update_region(
    *,
    region_id: int,
    updated_by: User,
    code: Optional[str] = None,
    name: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Region:

    region = selectors.get_region_by_id(
        region_id=region_id
    )

    if not region:
        raise ValidationError("Region not found.")

    if code is not None:
        code = _normalize(code).upper()
        _validate_region_uniqueness(
            country_id=region.country_id,
            code=code,
            exclude_region_id=region.id,
        )
        region.code = code

    if name is not None:
        region.name = _normalize(name)

    if is_active is not None:
        region.is_active = is_active

    region.updated_by = updated_by
    region.save(update_fields=[
        "code",
        "name",
        "is_active",
        "updated_by",
        "updated_at",
    ])

    return region


@transaction.atomic
def delete_region(
    *,
    region_id: int,
    deleted_by: User,
) -> None:

    region = selectors.get_region_by_id(
        region_id=region_id
    )

    if not region:
        raise ValidationError("Region not found.")

    region.is_deleted = True
    region.updated_by = deleted_by
    region.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
