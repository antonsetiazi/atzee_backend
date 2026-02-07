# accounting/fiscal_period/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError
from accounting.fiscal_period.models import FiscalPeriod
from accounting.fiscal_period import selectors
from core.tenants.models import Tenant
from core.users.models import User
from accounting.fiscal_period.models import FiscalPeriod
from accounting.fiscal_period.closing import close_fiscal_period_logic  # existing logic


@transaction.atomic
def create_fiscal_period(
    *,
    tenant: Tenant,
    created_by: User,
    name: str,
    start_date,
    end_date,
) -> FiscalPeriod:
    name = name.strip()

    # VALIDATION
    qs = selectors.get_fiscal_period_queryset(tenant=tenant)
    overlap = qs.filter(
        start_date__lte=end_date,
        end_date__gte=start_date
    ).exists()
    if overlap:
        raise ValidationError("Fiscal period overlaps with existing period.")

    period = FiscalPeriod.objects.create(
        tenant=tenant,
        name=name,
        start_date=start_date,
        end_date=end_date,
        created_by=created_by
    )
    return period


@transaction.atomic
def update_fiscal_period(
    *,
    tenant: Tenant,
    period_id,
    updated_by: User,
    name: Optional[str] = None,
    start_date = None,
    end_date = None,
) -> FiscalPeriod:
    period = selectors.get_fiscal_period_by_id(tenant=tenant, period_id=period_id)
    if not period:
        raise ValidationError("Fiscal period not found.")
    if period.is_closed:
        raise ValidationError("Cannot edit closed period.")

    # VALIDATION
    qs = selectors.get_fiscal_period_queryset(tenant=tenant).exclude(id=period.id)
    overlap = qs.filter(
        start_date__lte=end_date or period.end_date,
        end_date__gte=start_date or period.start_date
    ).exists()
    if overlap:
        raise ValidationError("Fiscal period overlaps with existing period.")

    if name:
        period.name = name
    if start_date:
        period.start_date = start_date
    if end_date:
        period.end_date = end_date

    period.updated_by = updated_by
    period.save(update_fields=["name", "start_date", "end_date", "updated_by", "updated_at"])

    return period


@transaction.atomic
def close_fiscal_period(*, tenant: Tenant, period_id, closed_by: User):
    period = selectors.get_fiscal_period_by_id(tenant=tenant, period_id=period_id)
    if not period:
        raise ValidationError("Fiscal period not found.")

    if period.is_closed:
        raise ValidationError("Fiscal period already closed.")

    # Panggil logic close existing
    close_fiscal_period_logic(
        tenant=tenant,
        period=period,
        closed_by=closed_by
    )
    return period
