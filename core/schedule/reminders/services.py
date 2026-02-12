# core/schedule/reminders/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.schedule.reminders.models import Reminder
from core.schedule.reminders import selectors
from core.schedule.events import selectors as event_selectors
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_reminder(
    *,
    tenant: Tenant,
    created_by: User,
    event: int,
    reminder_time,
    reminder_type: str,
    repeat_interval=None,
) -> Reminder:

    event_obj = event_selectors.get_event_by_id(
        tenant=tenant,
        event_id=event
    )

    if not event_obj:
        raise ValidationError("Event not found.")

    reminder = Reminder.objects.create(
        tenant=tenant,
        created_by=created_by,
        event=event_obj,
        reminder_time=reminder_time,
        reminder_type=reminder_type,
        repeat_interval=repeat_interval,
    )

    return reminder


@transaction.atomic
def update_reminder(
    *,
    tenant: Tenant,
    reminder_id: int,
    updated_by: User,
    reminder_time=None,
    reminder_type: Optional[str] = None,
    repeat_interval=None,
) -> Reminder:

    reminder = selectors.get_reminder_by_id(
        tenant=tenant,
        reminder_id=reminder_id
    )

    if not reminder:
        raise ValidationError("Reminder not found.")

    if reminder_time is not None:
        reminder.reminder_time = reminder_time

    if reminder_type is not None:
        reminder.reminder_type = reminder_type

    if repeat_interval is not None:
        reminder.repeat_interval = repeat_interval

    reminder.updated_by = updated_by
    reminder.save(update_fields=[
        "reminder_time",
        "reminder_type",
        "repeat_interval",
        "updated_by",
        "updated_at",
    ])

    return reminder


@transaction.atomic
def delete_reminder(
    *,
    tenant: Tenant,
    reminder_id: int,
    deleted_by: User
):
    reminder = selectors.get_reminder_by_id(
        tenant=tenant,
        reminder_id=reminder_id
    )

    if not reminder:
        raise ValidationError("Reminder not found.")

    reminder.is_deleted = True
    reminder.updated_by = deleted_by
    reminder.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
