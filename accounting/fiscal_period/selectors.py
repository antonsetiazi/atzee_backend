# accounting/fiscal_period/selectors.py

from typing import Optional
from accounting.fiscal_period.models import FiscalPeriod
from core.tenants.models import Tenant


def get_fiscal_period_queryset(*, tenant: Tenant):
    return FiscalPeriod.objects.filter(tenant=tenant).order_by("start_date")


def get_fiscal_period_by_id(*, tenant: Tenant, period_id) -> Optional[FiscalPeriod]:
    try:
        return get_fiscal_period_queryset(tenant=tenant).get(id=period_id)
    except FiscalPeriod.DoesNotExist:
        return None


def get_active_period(*, tenant: Tenant) -> Optional[FiscalPeriod]:
    return (
        get_fiscal_period_queryset(tenant=tenant)
        .filter(is_closed=False)
        .order_by("start_date")
        .first()
    )


def fiscal_period_exists(*, tenant: Tenant, period_id) -> bool:
    return get_fiscal_period_queryset(tenant=tenant).filter(id=period_id).exists()
