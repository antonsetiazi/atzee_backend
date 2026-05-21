# hrms/services/attendance/detect_absence.py

from hrms.enums import AttendanceStatus
from hrms.models import Attendance, Employee


def detect_absence(
    *,
    tenant,
    attendance_date,
):
    """
    Detect employees without attendance.
    """

    employees = Employee.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True,
    )

    attendance_employee_ids = Attendance.objects.filter(
        tenant=tenant,
        attendance_date=attendance_date,
        is_deleted=False,
    ).values_list(
        "employee_id",
        flat=True,
    )

    absent_employees = employees.exclude(id__in=attendance_employee_ids)

    created_records = []

    for employee in absent_employees:

        attendance, created = Attendance.objects.get_or_create(
            tenant=tenant,
            employee=employee,
            attendance_date=attendance_date,
            defaults={
                "status": AttendanceStatus.ABSENT,
            },
        )

        if created:
            created_records.append(attendance)

    return created_records
