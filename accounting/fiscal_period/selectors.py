from accounting.fiscal_period.models import FiscalPeriod
from core.tenants.models import Tenant


def get_active_period(*, tenant: Tenant) -> FiscalPeriod | None:
    return (
        FiscalPeriod.objects
        .filter(
            tenant=tenant,
            is_closed=False
        )
        .order_by("start_date")
        .first()
    )