# core/schedule/services/holiday_service.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.schedule.holidays.models import Holiday
from core.schedule.holidays import selectors
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_holiday(
    *,
    tenant: Tenant,
    created_by: User,
    name: str,
    start_datetime,
    end_datetime,
    all_day: bool = True,
    recurring: bool = False,
    metadata: Optional[dict] = None
) -> Holiday:
    
    if start_datetime >= end_datetime:
        raise ValidationError(
            "start_datetime must be before end_datetime."
        )

    holiday = Holiday.objects.create(
        tenant=tenant,
        created_by=created_by,
        name=name.strip(),
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        all_day=all_day,
        recurring=recurring,
        metadata=metadata or {}
    )
    return holiday


@transaction.atomic
def update_holiday(
    *,
    tenant: Tenant,
    holiday_id: int,
    updated_by: User,
    name: Optional[str] = None,
    start_datetime=None,
    end_datetime=None,
    all_day: Optional[bool] = None,
    recurring: Optional[bool] = None,
    metadata: Optional[dict] = None
) -> Holiday:
    holiday = selectors.get_holiday_by_id(tenant=tenant, holiday_id=holiday_id)
    if not holiday:
        raise ValidationError("Holiday not found.")

    if name is not None:
        holiday.name = name.strip()
    if start_datetime is not None:
        holiday.start_datetime = start_datetime
    if end_datetime is not None:
        holiday.end_datetime = end_datetime
    if all_day is not None:
        holiday.all_day = all_day
    if recurring is not None:
        holiday.recurring = recurring
    if metadata is not None:
        holiday.metadata = metadata

    holiday.updated_by = updated_by
    holiday.save(update_fields=[
        "name", "start_datetime", "end_datetime", "all_day",
        "recurring", "metadata", "updated_by", "updated_at"
    ])
    return holiday


@transaction.atomic
def delete_holiday(*, tenant: Tenant, holiday_id: int, deleted_by: User):
    holiday = selectors.get_holiday_by_id(tenant=tenant, holiday_id=holiday_id)
    if not holiday:
        raise ValidationError("Holiday not found.")

    holiday.is_deleted = True
    holiday.updated_by = deleted_by
    holiday.save(update_fields=["is_deleted", "updated_by", "updated_at"])
