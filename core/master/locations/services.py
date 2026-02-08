# core/master/locations/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.master.locations.models import Location
from core.master.locations import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_code_uniqueness(
    *,
    tenant: Tenant,
    code: str,
    exclude_id: Optional[int] = None
) -> None:
    qs = Location.objects.filter(
        tenant=tenant,
        is_deleted=False,
        code=code
    )
    if exclude_id:
        qs = qs.exclude(id=exclude_id)

    if qs.exists():
        raise ValidationError("Location with this code already exists.")


@transaction.atomic
def create_location(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    description: Optional[str] = "",
    parent_id: Optional[int] = None,
    is_active: bool = True,
) -> Location:
    code = _normalize(code)
    name = _normalize(name)
    description = _normalize(description)

    if not code or not name:
        raise ValidationError("Code and name are required.")

    _validate_code_uniqueness(
        tenant=tenant,
        code=code
    )

    parent = None
    if parent_id:
        parent = selectors.get_location_by_id(
            tenant=tenant,
            location_id=parent_id
        )
        if not parent:
            raise ValidationError("Parent location not found.")

    location = Location.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        description=description,
        parent=parent,
        is_active=is_active,
        created_by=created_by
    )

    return location


@transaction.atomic
def update_location(
    *,
    tenant: Tenant,
    location_id: int,
    updated_by: User,
    name: Optional[str] = None,
    description: Optional[str] = None,
    parent_id: Optional[int] = None,
    is_active: Optional[bool] = None,
) -> Location:
    location = selectors.get_location_by_id(
        tenant=tenant,
        location_id=location_id
    )

    if not location:
        raise ValidationError("Location not found.")

    if name is not None:
        location.name = _normalize(name)

    if description is not None:
        location.description = _normalize(description)

    if parent_id is not None:
        if parent_id == location.id:
            raise ValidationError("Location cannot be parent of itself.")

        parent = None
        if parent_id:
            parent = selectors.get_location_by_id(
                tenant=tenant,
                location_id=parent_id
            )
            if not parent:
                raise ValidationError("Parent location not found.")

        location.parent = parent

    if is_active is not None:
        location.is_active = is_active

    location.updated_by = updated_by
    location.save(update_fields=[
        "name",
        "description",
        "parent",
        "is_active",
        "updated_by",
        "updated_at",
    ])

    return location


@transaction.atomic
def delete_location(
    *,
    tenant: Tenant,
    location_id: int,
    deleted_by: User
) -> None:
    location = selectors.get_location_by_id(
        tenant=tenant,
        location_id=location_id
    )

    if not location:
        raise ValidationError("Location not found.")

    if location.children.exists():
        raise ValidationError(
            "Cannot delete location with child locations."
        )

    location.is_deleted = True
    location.updated_by = deleted_by
    location.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
