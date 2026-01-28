from datetime import date, datetime
from typing import Optional

from django.db import transaction
from django.core.exceptions import ValidationError

from hr.attendance.models import AttendanceRecord
from hr.attendance import selectors
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_attendance(
    *,
    tenant: Tenant,
    created_by: User,
    employee_id: int,
    work_date: date,
    status: str = AttendanceRecord.STATUS_PRESENT,
    check_in: Optional[datetime] = None,
    check_out: Optional[datetime] = None,
    notes: Optional[str] = None
) -> AttendanceRecord:
    """
    Create daily attendance record.
    One per employee per date.
    """

    existing = selectors.get_attendance_by_employee_and_date(
        tenant=tenant,
        employee_id=employee_id,
        work_date=work_date
    )

    if existing:
        raise ValidationError(
            "Attendance already exists for this date."
        )
    
    attendance = AttendanceRecord.objects.create(
        tenant=tenant,
        employee_id=employee_id,
        date=work_date,
        status=status,
        check_in=check_in,
        check_out=check_out,
        notes=notes,
        created_by=created_by
    )

    return attendance


@transaction.atomic
def update_attendance(
    *,
    tenant: Tenant,
    attendance_id: int,
    updated_by: User,
    status: Optional[str] = None,
    check_in: Optional[datetime] = None,
    check_out: Optional[datetime] = None,
    notes: Optional[str] = None,
) -> AttendanceRecord:
    """
    Limited mutation (correction).
    """

    attendance = selectors.get_attendance_by_id(
        tenant=tenant,
        attendance_id=attendance_id
    )

    if not attendance:
        raise ValidationError("Attendance not found.")
    
    if status is not None:
        attendance.status = status
    if check_in is not None:
        attendance.check_in = check_in
    if check_out is not None:
        attendance.check_out = check_out
    if notes is not None:
        attendance.notes = notes

    attendance.updated_by = updated_by
    attendance.save(update_fields=[
        "status",
        "check_in",
        "check_out",
        "notes",
        "updated_by",
        "updated_at",
    ])

    return attendance


@transaction.atomic
def delete_attendance(
    *,
    tenant: Tenant,
    attendance_id: int,
    deleted_by: User
) -> None:
    """
    Soft delete attendance (rare, audit reason).
    """

    attendance = selectors.get_attendance_by_id(
        tenant=tenant,
        attendance_id=attendance_id
    )

    if not attendance:
        raise ValidationError("Attendance not found.")
    
    attendance.is_deleted = True
    attendance.updated_by = deleted_by
    attendance.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at",
    ])