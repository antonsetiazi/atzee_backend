# core/schedule/holidays/selectors.py

from typing import Optional
from core.schedule.holidays.models import Holiday
from core.tenants.models import Tenant


def get_holiday_queryset(*, tenant: Tenant):
    return Holiday.objects.filter(tenant=tenant, is_deleted=False)


def get_holiday_by_id(*, tenant: Tenant, holiday_id: int) -> Optional[Holiday]:
    try:
        return Holiday.objects.get(tenant=tenant, id=holiday_id, is_deleted=False)
    except Holiday.DoesNotExist:
        return None
