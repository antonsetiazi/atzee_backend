# core/schedule/recurring/selectors.py

from typing import Optional
from core.schedule.recurrings.models import Recurring
from core.tenants.models import Tenant


def get_recurring_queryset(*, tenant: Tenant):
    return Recurring.objects.filter(
        tenant=tenant,
        is_deleted=False
    ).select_related("event")


def get_recurring_by_id(
    *,
    tenant: Tenant,
    recurring_id: int
) -> Optional[Recurring]:
    try:
        return Recurring.objects.select_related("event").get(
            tenant=tenant,
            id=recurring_id,
            is_deleted=False
        )
    except Recurring.DoesNotExist:
        return None

