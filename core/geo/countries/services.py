# core/geo/countries/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError
from core.geo.countries.models import Country
from core.geo.countries import selectors
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    """
    Domain rule:
    - None -> ""
    - strip whitespace
    """
    return value.strip() if isinstance(value, str) else ""


def _validate_country_uniqueness(
        *, 
        code: Optional[str],
        exclude_country_id: Optional[int] = None
) -> None:
    """
    Prevent duplicate country by code or phone within tenant.
    """

    qs = selectors.get_country_queryset()

    if exclude_country_id:
        qs = qs.exclude(id=exclude_country_id)
    
    if code and qs.filter(code=code).exists():
        raise ValidationError("Country with this code already exists.")


@transaction.atomic
def create_country(
    *,
    created_by: User,
    code: str,
    name: str,
    phone_code: str = "",
    currency_code: str = "",
) -> Country:

    code = code.upper().strip()

    if Country.objects.filter(
        code=code,
        is_deleted=False
    ).exists():
        raise ValidationError("Country already exists.")

    return Country.objects.create(
        code=code,
        name=name.strip(),
        phone_code=phone_code.strip(),
        currency_code=currency_code.strip(),
        created_by=created_by,
    )


def update_country(
    *,
    country_id: int,
    updated_by: User,
    name: Optional[str] = None,
    code: Optional[str] = None,
    phone_code: Optional[str] = None,
    currency_code: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Country:
    """
    Update existing country.
    """

    country = selectors.get_country_by_id(
        country_id=country_id
    )

    if not country:
        raise ValidationError("Country not found.")
    
    _validate_country_uniqueness(
        code=code,
        exclude_country_id=country.id
    )

    if name is not None:
        country.name = name
    if code is not None:
        code = code.upper().strip()
        country.code = code
    if phone_code is not None:
        country.phone_code = phone_code
    if currency_code is not None:
        country.currency_code = currency_code
    if is_active is not None:
        country.is_active = is_active

    country.updated_by = updated_by
    country.save(update_fields=[
        "name",
        "code",
        "phone_code",
        "currency_code",
        "is_active",
        "updated_by",
        "updated_at"
    ])

    return country


@transaction.atomic
def delete_country(
    *,
    country_id: int,
    deleted_by: User
) -> None:
    """
    Soft delete country.
    """
    
    country = selectors.get_country_by_id(
        country_id=country_id
    )
    
    if not country:
        raise ValidationError("Country not found")

    country.is_deleted = True
    country.updated_by = deleted_by
    country.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])