# hrms/workflows/leave/leave_approval_workflow.py

from hrms.enums import LeaveStatus


def can_approve_leave(
    *,
    leave_request,
):
    """
    Validate leave approval workflow.
    """

    return leave_request.status == LeaveStatus.PENDING


def can_reject_leave(
    *,
    leave_request,
):
    """
    Validate leave rejection workflow.
    """

    return leave_request.status == LeaveStatus.PENDING
