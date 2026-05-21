# hrms/services/leave/apply_leave.py

from django.db import transaction

from hrms.enums import LeaveStatus
from hrms.models import LeaveRequest
from hrms.services.leave.calculate_leave_days import (
    calculate_leave_days,
)
from hrms.services.leave.validate_leave_balance import (
    validate_leave_balance,
)
from hrms.services.leave.validate_leave_overlap import (
    validate_leave_overlap,
)


@transaction.atomic
def apply_leave(
    *,
    tenant,
    employee,
    leave_type,
    start_date,
    end_date,
    reason="",
    created_by=None,
):
    """
    Apply employee leave request.
    """

    is_valid_overlap = validate_leave_overlap(
        tenant=tenant,
        employee=employee,
        start_date=start_date,
        end_date=end_date,
    )

    if not is_valid_overlap:
        raise ValueError("Employee already has overlapping leave request.")

    requested_days = calculate_leave_days(
        start_date,
        end_date,
    )

    has_balance = validate_leave_balance(
        employee=employee,
        leave_type=leave_type,
        requested_days=requested_days,
    )

    if not has_balance:
        raise ValueError("Insufficient leave balance.")

    leave_request = LeaveRequest.objects.create(
        tenant=tenant,
        employee=employee,
        leave_type=leave_type,
        start_date=start_date,
        end_date=end_date,
        reason=reason,
        status=LeaveStatus.PENDING,
        created_by=created_by,
        updated_by=created_by,
    )

    # future:
    # approval workflow
    # notification
    # activity log
    # calendar sync

    return leave_request
