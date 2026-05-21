# hrms/services/leave/reject_leave.py

from django.db import transaction

from hrms.enums import LeaveStatus


@transaction.atomic
def reject_leave(*, leave_request, rejected_by):
    """
    Reject leave request.
    """

    leave_request.status = LeaveStatus.REJECTED
    leave_request.updated_by = rejected_by.user if rejected_by.user else None
    leave_request.save()

    return leave_request
