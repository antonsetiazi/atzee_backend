# hrms/workflows/leave/__init__.py

from .leave_approval_workflow import (
    can_approve_leave,
    can_reject_leave,
)
from .leave_policy_workflow import (
    requires_manager_approval,
)

__all__ = [
    "can_approve_leave",
    "can_reject_leave",
    "requires_manager_approval",
]
