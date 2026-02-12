# core/schedule/recurrings/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.schedule.recurrings.models import Recurring
from core.schedule.recurrings import selectors
from core.schedule.events import selectors as event_selectors
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_recurring(
    *,
    tenant: Tenant,
    created_by: User,
    event: int,
    frequency: str,
    interval: int = 1,
    end_date=None,
) -> Recurring:

    event_obj = event_selectors.get_event_by_id(
        tenant=tenant,
        event_id=event
    )

    if not event_obj:
        raise ValidationError("Event not found.")

    recurring = Recurring.objects.create(
        tenant=tenant,
        created_by=created_by,
        event=event_obj,
        frequency=frequency,
        interval=interval,
        end_date=end_date,
    )

    return recurring


@transaction.atomic
def update_recurring(
    *,
    tenant: Tenant,
    recurring_id: int,
    updated_by: User,
    frequency: Optional[str] = None,
    interval: Optional[int] = None,
    end_date=None,
) -> Recurring:

    recurring = selectors.get_recurring_by_id(
        tenant=tenant,
        recurring_id=recurring_id
    )

    if not recurring:
        raise ValidationError("Recurring not found.")

    if frequency is not None:
        recurring.frequency = frequency

    if interval is not None:
        recurring.interval = interval

    if end_date is not None:
        recurring.end_date = end_date

    recurring.updated_by = updated_by
    recurring.save(update_fields=[
        "frequency",
        "interval",
        "end_date",
        "updated_by",
        "updated_at",
    ])

    return recurring


@transaction.atomic
def delete_recurring(
    *,
    tenant: Tenant,
    recurring_id: int,
    deleted_by: User
):

    recurring = selectors.get_recurring_by_id(
        tenant=tenant,
        recurring_id=recurring_id
    )

    if not recurring:
        raise ValidationError("Recurring not found.")

    recurring.is_deleted = True
    recurring.updated_by = deleted_by
    recurring.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])
