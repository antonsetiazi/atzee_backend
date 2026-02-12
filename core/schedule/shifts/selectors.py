# core/schedule/shifts/selectors.py

from typing import Optional

from core.schedule.shifts.models import Shift
from core.tenants.models import Tenant


def get_shift_queryset(*, tenant: Tenant):
    return (
        Shift.objects
        .filter(tenant=tenant, is_deleted=False)
        .select_related("created_by", "updated_by")
        .prefetch_related("participants")
        .order_by("start_datetime")
    )


def get_shift_by_id(*, tenant: Tenant, shift_id: int) -> Optional[Shift]:
    try:
        return (
            Shift.objects
            .select_related("created_by", "updated_by")
            .prefetch_related("participants")
            .get(tenant=tenant, id=shift_id, is_deleted=False)
        )
    except Shift.DoesNotExist:
        return None

