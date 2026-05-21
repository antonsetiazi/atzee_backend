# hrms/selectors/attendance_selector.py

from django.db.models import Count

from hrms.enums import AttendanceStatus
from hrms.models import Attendance


def get_employee_attendance_history(
    tenant,
    employee_id,
):
    return Attendance.objects.filter(
        tenant=tenant,
        employee_id=employee_id,
        is_deleted=False,
    ).order_by("-attendance_date")


def get_today_attendance(
    tenant,
    attendance_date,
):
    return Attendance.objects.filter(
        tenant=tenant,
        attendance_date=attendance_date,
        is_deleted=False,
    ).select_related(
        "employee",
    )


def get_absent_employees(
    tenant,
    attendance_date,
):
    return Attendance.objects.filter(
        tenant=tenant,
        attendance_date=attendance_date,
        status=AttendanceStatus.ABSENT,
        is_deleted=False,
    ).select_related(
        "employee",
    )


def get_attendance_summary(
    tenant,
    attendance_date,
):
    return (
        Attendance.objects.filter(
            tenant=tenant,
            attendance_date=attendance_date,
            is_deleted=False,
        )
        .values(
            "status",
        )
        .annotate(total=Count("id"))
    )
