# hrms/services/attendance/check_in.py

from django.db import transaction
from django.utils import timezone

from hrms.enums import AttendanceStatus
from hrms.models import Attendance


@transaction.atomic
def check_in(
    *,
    tenant,
    employee,
    attendance_date,
    check_in_time=None,
    notes="",
    created_by=None,
):
    """
    Employee attendance check-in.
    """

    attendance, created = Attendance.objects.get_or_create(
        tenant=tenant,
        employee=employee,
        attendance_date=attendance_date,
        defaults={
            "check_in": check_in_time or timezone.now(),
            "status": AttendanceStatus.PRESENT,
            "notes": notes,
            "created_by": created_by,
            "updated_by": created_by,
        },
    )

    if not created:
        attendance.check_in = check_in_time or timezone.now()

        attendance.updated_by = created_by

        attendance.save()

    # future:
    # late detection
    # geofence validation
    # biometric validation
    # activity log

    return attendance
