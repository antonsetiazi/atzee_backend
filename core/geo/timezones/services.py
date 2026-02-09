# core/geo/timezones/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.geo.timezones.models import Timezone
from core.geo.timezones import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_timezone_uniqueness(
    *,
    tenant: Tenant,
    name: Optional[str],
    exclude_timezone_id: Optional[int] = None,
) -> None:
    qs = selectors.get_timezone_queryset(tenant=tenant)

    if exclude_timezone_id:
        qs = qs.exclude(id=exclude_timezone_id)

    if name and qs.filter(name=name).exists():
        raise ValidationError("Timezone with this name already exists.")


@transaction.atomic
def create_timezone(
    *,
    tenant: Tenant,
    created_by: User,
    name: str,
    utc_offset: str,
) -> Timezone:

    name = _normalize_str(name)

    if selectors.get_timezone_queryset(
        tenant=tenant
    ).filter(name=name).exists():
        raise ValidationError("Timezone already exists.")

    return Timezone.objects.create(
        tenant=tenant,
        name=name,
        utc_offset=_normalize_str(utc_offset),
        created_by=created_by,
    )


@transaction.atomic
def update_timezone(
    *,
    tenant: Tenant,
    timezone_id: int,
    updated_by: User,
    name: Optional[str] = None,
    utc_offset: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Timezone:

    timezone = selectors.get_timezone_by_id(
        tenant=tenant,
        timezone_id=timezone_id,
    )

    if not timezone:
        raise ValidationError("Timezone not found.")

    _validate_timezone_uniqueness(
        tenant=tenant,
        name=name,
        exclude_timezone_id=timezone.id,
    )

    if name is not None:
        timezone.name = _normalize_str(name)
    if utc_offset is not None:
        timezone.utc_offset = _normalize_str(utc_offset)
    if is_active is not None:
        timezone.is_active = is_active

    timezone.updated_by = updated_by
    timezone.save(update_fields=[
        "name",
        "utc_offset",
        "is_active",
        "updated_by",
        "updated_at",
    ])

    return timezone


@transaction.atomic
def delete_timezone(
    *,
    tenant: Tenant,
    timezone_id: int,
    deleted_by: User,
) -> None:
    timezone = selectors.get_timezone_by_id(
        tenant=tenant,
        timezone_id=timezone_id,
    )

    if not timezone:
        raise ValidationError("Timezone not found.")

    timezone.is_deleted = True
    timezone.updated_by = deleted_by
    timezone.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
