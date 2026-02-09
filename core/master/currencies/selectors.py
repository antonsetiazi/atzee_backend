# core/master/currencies/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.master.currencies.models import Currency
from core.tenants.models import Tenant


def get_currency_queryset(*, tenant: Tenant) -> QuerySet[Currency]:
    return Currency.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True
    )


def get_currencies(*, tenant: Tenant) -> QuerySet[Currency]:
    return get_currency_queryset(tenant=tenant).order_by("code")


def get_currency_by_id(
    *, tenant: Tenant, currency_id: int
) -> Optional[Currency]:
    try:
        return get_currency_queryset(
            tenant=tenant
        ).get(id=currency_id)
    except Currency.DoesNotExist:
        return None


def get_currency_by_code(
    *, tenant: Tenant, code: str
) -> Optional[Currency]:
    try:
        return get_currency_queryset(
            tenant=tenant
        ).get(code=code)
    except Currency.DoesNotExist:
        return None
