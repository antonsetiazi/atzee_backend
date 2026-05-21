# hrms/workflows/__init__.py

from .employee import (
    can_onboard_employee,
    can_promote_employee,
    can_terminate_employee,
)
from .leave import (
    can_approve_leave,
    can_reject_leave,
    requires_manager_approval,
)
from .payroll import (
    can_approve_payroll,
    can_post_payroll,
)

__all__ = [
    "can_onboard_employee",
    "can_promote_employee",
    "can_terminate_employee",
    "can_approve_leave",
    "can_reject_leave",
    "requires_manager_approval",
    "can_approve_payroll",
    "can_post_payroll",
]
