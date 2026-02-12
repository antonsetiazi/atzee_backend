# core/schedule/selectors.py

from typing import Optional
from core.schedule.reminders.models import Reminder
from core.tenants.models import Tenant


def get_reminder_queryset(*, tenant: Tenant):
    return Reminder.objects.filter(tenant=tenant, is_deleted=False)


def get_reminder_by_id(*, tenant: Tenant, reminder_id: int) -> Optional[Reminder]:
    try:
        return Reminder.objects.get(tenant=tenant, id=reminder_id, is_deleted=False)
    except Reminder.DoesNotExist:
        return None
