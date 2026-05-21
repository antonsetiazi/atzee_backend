# hrms/services/leave/validate_leave_overlap.py

from hrms.enums import LeaveStatus
from hrms.models import LeaveRequest


def validate_leave_overlap(
    *,
    tenant,
    employee,
    start_date,
    end_date,
):
    """
    Validate overlapping leave request.
    """

    overlapping_leave = LeaveRequest.objects.filter(
        tenant=tenant,
        employee=employee,
        status__in=[
            LeaveStatus.PENDING,
            LeaveStatus.APPROVED,
        ],
        start_date__lte=end_date,
        end_date__gte=start_date,
        is_deleted=False,
    ).exists()

    return not overlapping_leave
