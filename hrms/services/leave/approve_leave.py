# hrms/services/leave/approve_leave.py

from django.db import transaction
from django.utils import timezone

from hrms.enums import LeaveStatus


@transaction.atomic
def approve_leave(
    *,
    leave_request,
    approved_by,
):
    """
    Approve employee leave request.
    """

    leave_request.status = LeaveStatus.APPROVED
    leave_request.approved_by = approved_by
    leave_request.approved_at = timezone.now()
    leave_request.updated_by = approved_by.user if approved_by.user else None
    leave_request.save()

    # future:
    # attendance sync
    # payroll sync
    # notification
    # activity log

    return leave_request
