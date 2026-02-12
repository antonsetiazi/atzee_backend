# core/schedule/shifts/services.py

from typing import Optional, List
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.schedule.shifts.models import Shift
from core.schedule.shifts import selectors 
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_shift(
    *,
    tenant: Tenant,
    created_by: User,
    name: str,
    start_datetime,
    end_datetime,
    participants: Optional[List[int]] = None,
    rotation_pattern: Optional[dict] = None,
    metadata: Optional[dict] = None
) -> Shift:
    shift = Shift.objects.create(
        tenant=tenant,
        created_by=created_by,
        name=name.strip(),
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        participants=participants or [],
        rotation_pattern=rotation_pattern or {},
        metadata=metadata or {}
    )
    return shift


@transaction.atomic
def update_shift(
    *,
    tenant: Tenant,
    shift_id: int,
    updated_by: User,
    name: Optional[str] = None,
    start_datetime=None,
    end_datetime=None,
    participants: Optional[List[int]] = None,
    rotation_pattern: Optional[dict] = None,
    metadata: Optional[dict] = None
) -> Shift:
    shift = selectors.get_shift_by_id(tenant=tenant, shift_id=shift_id)
    if not shift:
        raise ValidationError("Shift not found.")

    if name is not None:
        shift.name = name.strip()
    if start_datetime is not None:
        shift.start_datetime = start_datetime
    if end_datetime is not None:
        shift.end_datetime = end_datetime
    if participants is not None:
        shift.participants = participants
    if rotation_pattern is not None:
        shift.rotation_pattern = rotation_pattern
    if metadata is not None:
        shift.metadata = metadata

    shift.updated_by = updated_by
    shift.save(update_fields=[
        "name", "start_datetime", "end_datetime", "participants",
        "rotation_pattern", "metadata", "updated_by", "updated_at"
    ])
    return shift


@transaction.atomic
def delete_shift(*, tenant: Tenant, shift_id: int, deleted_by: User):
    shift = selectors.get_shift_by_id(tenant=tenant, shift_id=shift_id)
    if not shift:
        raise ValidationError("Shift not found.")

    shift.is_deleted = True
    shift.updated_by = deleted_by
    shift.save(update_fields=["is_deleted", "updated_by", "updated_at"])
