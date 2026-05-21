# hrms/services/leave/cancel_leave.py

from django.db import transaction

from hrms.enums import LeaveStatus


@transaction.atomic
def cancel_leave(*, leave_request, cancelled_by):
    """
    Cancel leave request.
    """

    leave_request.status = LeaveStatus.CANCELLED
    leave_request.updated_by = cancelled_by.user if cancelled_by.user else None
    leave_request.save()

    return leave_request
