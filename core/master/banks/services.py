# core/master/banks/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.master.banks.models import Bank
from core.master.banks import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_uniqueness(
    *,
    tenant: Tenant,
    code: Optional[str],
    name: Optional[str],
    exclude_id: Optional[int] = None,
) -> None:
    qs = selectors.get_bank_queryset(tenant=tenant)

    if exclude_id:
        qs = qs.exclude(id=exclude_id)

    if code and qs.filter(code=code).exists():
        raise ValidationError("Bank with this code already exists.")

    if name and qs.filter(name=name).exists():
        raise ValidationError("Bank with this name already exists.")


@transaction.atomic
def create_bank(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    short_name: str = "",
) -> Bank:

    code = _normalize(code)
    name = _normalize(name)
    short_name = _normalize(short_name)

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        name=name,
    )

    return Bank.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        short_name=short_name,
        created_by=created_by,
    )


@transaction.atomic
def update_bank(
    *,
    tenant: Tenant,
    bank_id: int,
    updated_by: User,
    code: Optional[str] = None,
    name: Optional[str] = None,
    short_name: Optional[str] = None,
    sort_order: Optional[int] = None,
    is_active: Optional[bool] = None,
) -> Bank:

    bank = selectors.get_bank_by_id(
        tenant=tenant,
        bank_id=bank_id,
    )

    if not bank:
        raise ValidationError("Bank not found.")

    _validate_uniqueness(
        tenant=tenant,
        code=code,
        name=name,
        exclude_id=bank.id,
    )

    if code is not None:
        bank.code = _normalize(code)

    if name is not None:
        bank.name = _normalize(name)

    if short_name is not None:
        bank.short_name = _normalize(short_name)

    if sort_order is not None:
        bank.sort_order = sort_order

    if is_active is not None:
        bank.is_active = is_active

    bank.updated_by = updated_by
    bank.save()

    return bank


@transaction.atomic
def delete_bank(
    *,
    tenant: Tenant,
    bank_id: int,
    deleted_by: User,
) -> None:

    bank = selectors.get_bank_by_id(
        tenant=tenant,
        bank_id=bank_id,
    )

    if not bank:
        raise ValidationError("Bank not found.")

    bank.is_deleted = True
    bank.updated_by = deleted_by
    bank.save()