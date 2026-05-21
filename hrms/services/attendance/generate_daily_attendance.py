# hrms/services/attendance/generate_daily_attendance.py

from hrms.enums import AttendanceStatus
from hrms.models import Attendance, Employee


def generate_daily_attendance(
    *,
    tenant,
    attendance_date,
):
    """
    Generate initial attendance records
    for active employees.
    """

    employees = Employee.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True,
    )

    generated_records = []

    for employee in employees:

        attendance, created = Attendance.objects.get_or_create(
            tenant=tenant,
            employee=employee,
            attendance_date=attendance_date,
            defaults={
                "status": AttendanceStatus.ABSENT,
            },
        )

        if created:
            generated_records.append(attendance)

    return generated_records
