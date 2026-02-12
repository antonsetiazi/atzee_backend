# core/schedule/events/services.py

from typing import Optional, List
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.schedule.events.models import Event
from core.schedule.events import selectors 
from core.tenants.models import Tenant
from core.users.models import User


def _normalize_str(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""


def _validate_event_overlap(
    *, tenant: Tenant, start_datetime, end_datetime, exclude_event_id: Optional[int] = None
):
    """
    Prevent overlapping events in the same tenant
    """
    qs = selectors.get_event_queryset(tenant=tenant)
    if exclude_event_id:
        qs = qs.exclude(id=exclude_event_id)

    overlapping = qs.filter(
        start_datetime__lt=end_datetime,
        end_datetime__gt=start_datetime
    ).exists()

    if overlapping:
        raise ValidationError("Event overlaps with existing events.")


@transaction.atomic
def create_event(
    *,
    tenant: Tenant,
    created_by: User,
    title: str,
    start_datetime,
    end_datetime,
    description = None,
    all_day: bool = False,
    participants: Optional[List[int]] = None,
    color: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> Event:
    title = _normalize_str(title)

    # domain validation
    _validate_event_overlap(
        tenant=tenant,
        start_datetime=start_datetime,
        end_datetime=end_datetime
    )

    if start_datetime >= end_datetime:
        raise ValidationError("start_datetime must be before end_datetime.")


    event = Event.objects.create(
        tenant=tenant,
        created_by=created_by,
        title=title,
        description=description or "",
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        all_day=all_day,
        participants=participants or [],
        color=color,
        metadata=metadata or {}
    )
    return event


@transaction.atomic
def update_event(
    *,
    tenant: Tenant,
    event_id: int,
    updated_by: User,
    title: Optional[str] = None,
    description: Optional[str] = None,
    start_datetime=None,
    end_datetime=None,
    all_day: Optional[bool] = None,
    participants: Optional[List[int]] = None,
    color: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> Event:
    event = selectors.get_event_by_id(tenant=tenant, event_id=event_id)
    if not event:
        raise ValidationError("Event not found.")

    if title is not None:
        event.title = _normalize_str(title)
    if description is not None:
        event.description = _normalize_str(description)
    if start_datetime is not None:
        event.start_datetime = start_datetime
    if end_datetime is not None:
        event.end_datetime = end_datetime
    if all_day is not None:
        event.all_day = all_day
    if participants is not None:
        event.participants = participants
    if color is not None:
        event.color = color
    if metadata is not None:
        event.metadata = metadata

    # domain validation
    _validate_event_overlap(
        tenant=tenant,
        start_datetime=event.start_datetime,
        end_datetime=event.end_datetime,
        exclude_event_id=event.id
    )

    event.updated_by = updated_by
    event.save(update_fields=[
        "title", "description", "start_datetime", "end_datetime", "all_day",
        "participants", "color", "metadata", "updated_by", "updated_at"
    ])
    return event


@transaction.atomic
def delete_event(
    *, tenant: Tenant, event_id: int, deleted_by: User
):
    event = selectors.get_event_by_id(tenant=tenant, event_id=event_id)
    if not event:
        raise ValidationError("Event not found.")

    event.is_deleted = True
    event.updated_by = deleted_by
    event.save(update_fields=["is_deleted", "updated_by", "updated_at"])
