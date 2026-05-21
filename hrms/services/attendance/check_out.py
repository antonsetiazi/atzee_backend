# hrms/services/attendance/check_out.py

from django.db import transaction
from django.utils import timezone

# from hrms.models import Attendance


@transaction.atomic
def check_out(
    *,
    attendance,
    check_out_time=None,
    updated_by=None,
):
    """
    Employee attendance check-out.
    """

    attendance.check_out = check_out_time or timezone.now()
    attendance.updated_by = updated_by
    attendance.save()

    # future:
    # auto overtime
    # work hour calculation
    # payroll sync
    # activity log

    return attendance
