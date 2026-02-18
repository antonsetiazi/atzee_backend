# business/users/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from business.users.models import BusinessUser
from business.users import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


@transaction.atomic
def create_business_user(
    *,
    tenant: Tenant,
    core_user: User,
    created_by: User,
    name: str,
    phone: Optional[str] = None,
    email: Optional[str] = None,
    organization_name: Optional[str] = None,
    organization_type: Optional[str] = None,
    address: Optional[str] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    notes: Optional[str] = None,
    extensions: Optional[dict] = None,
) -> BusinessUser:

    if selectors.get_user_by_core_user(
        tenant=tenant,
        core_user_id=core_user.id
    ):
        raise ValidationError("Business profile already exists.")

    business_user = BusinessUser.objects.create(
        tenant=tenant,
        core_user=core_user,
        name=name.strip(),
        phone=_normalize_str(phone),
        email=_normalize_str(email),
        organization_name=_normalize_str(organization_name),
        organization_type=_normalize_str(organization_type),
        address=_normalize_str(address),
        latitude=latitude,
        longitude=longitude,
        notes=_normalize_str(notes),
        extensions=extensions or {},
        created_by=created_by
    )

    return business_user


@transaction.atomic
def update_business_user(
    *,
    tenant: Tenant,
    user_id: int,
    updated_by: User,
    **kwargs
) -> BusinessUser:

    user = selectors.get_user_by_id(
        tenant=tenant,
        user_id=user_id
    )

    if not user:
        raise ValidationError("Business user not found.")

    for field, value in kwargs.items():
        if hasattr(user, field) and value is not None:
            setattr(user, field, value)

    user.updated_by = updated_by
    user.save()

    return user
