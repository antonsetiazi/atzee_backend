# core/master/currencies/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.master.currencies.models import Currency
from core.master.currencies import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_code(value: str) -> str:
    return value.strip().upper()


@transaction.atomic
def create_currency(
    *,
    tenant: Tenant,
    created_by: User,
    code: str,
    name: str,
    symbol: Optional[str] = "",
    decimal_places: Optional[int] = 2,
) -> Currency:

    code = _normalize_code(code)
    name = name.strip()
    symbol = symbol.strip() if symbol else ""

    if Currency.objects.filter(
        tenant=tenant,
        code=code,
        is_deleted=False
    ).exists():
        raise ValidationError("Currency with this code already exists.")

    return Currency.objects.create(
        tenant=tenant,
        code=code,
        name=name,
        symbol=symbol,
        decimal_places=decimal_places or 2,
        created_by=created_by,
    )


@transaction.atomic
def update_currency(
    *,
    tenant: Tenant,
    currency_id: int,
    updated_by: User,
    name: Optional[str] = None,
    symbol: Optional[str] = None,
    decimal_places: Optional[int] = None,
    is_active: Optional[bool] = None,
) -> Currency:

    currency = selectors.get_currency_by_id(
        tenant=tenant,
        currency_id=currency_id
    )

    if not currency:
        raise ValidationError("Currency not found.")

    if name is not None:
        currency.name = name
    if symbol is not None:
        currency.symbol = symbol
    if decimal_places is not None:
        currency.decimal_places = decimal_places
    if is_active is not None:
        currency.is_active = is_active

    currency.updated_by = updated_by
    currency.save()

    return currency
