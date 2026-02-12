# core/schedule/events/selectors.py

from typing import Optional
from core.schedule.events.models import Event
from core.tenants.models import Tenant


def get_event_queryset(*, tenant: Tenant):
    return Event.objects.filter(tenant=tenant, is_deleted=False)


def get_event_by_id(*, tenant: Tenant, event_id: int) -> Optional[Event]:
    try:
        return Event.objects.get(tenant=tenant, id=event_id, is_deleted=False)
    except Event.DoesNotExist:
        return None
