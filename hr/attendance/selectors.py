from typing import Optional
from datetime import date
from django.db.models import QuerySet

from hr.attendance.models import AttendanceRecord
from core.tenants.models import Tenant


def get_attendance_queryset(
    *,
    tenant: Tenant
) -> QuerySet[AttendanceRecord]:
    return AttendanceRecord.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_attendance_by_id(
    *,
    tenant: Tenant,
    attendance_id: int
) -> Optional[AttendanceRecord]:
    try:
        return get_attendance_queryset(
            tenant=tenant
        ).get(id=attendance_id)
    except AttendanceRecord.DoesNotExist:
        return None
    

def get_attendance_by_employee_and_date(
    *,
    tenant: Tenant,
    employee_id: int,
    work_date: date
) -> Optional[AttendanceRecord]:
    try:
        return get_attendance_queryset(
            tenant=tenant
        ).get(
            employee_id=employee_id,
            date=work_date
        )
    except AttendanceRecord.DoesNotExist:
        return None
    

def get_employee_attendance(
    *,
    tenant: Tenant,
    employee_id: int,
    start_date: date,
    end_date: date
) -> QuerySet[AttendanceRecord]:
    return (
        get_attendance_queryset(tenant=tenant)
        .filter(
            employee_id=employee_id,
            date__range=(start_date, end_date)
        )
        .order_by("date")
    )