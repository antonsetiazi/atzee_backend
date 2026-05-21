# hrms/selectors/leave_selector.py

from hrms.enums import LeaveStatus
from hrms.models import LeaveRequest


def get_pending_leave_requests(
    tenant,
):
    return LeaveRequest.objects.filter(
        tenant=tenant,
        status=LeaveStatus.PENDING,
        is_deleted=False,
    ).select_related(
        "employee",
        "approved_by",
    )


def get_employee_leave_history(
    tenant,
    employee_id,
):
    return LeaveRequest.objects.filter(
        tenant=tenant,
        employee_id=employee_id,
        is_deleted=False,
    ).order_by("-created_at")
