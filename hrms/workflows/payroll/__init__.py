# hrms/workflows/payroll/__init__.py

from .payroll_approval_workflow import (
    can_approve_payroll,
)
from .payroll_posting_workflow import (
    can_post_payroll,
)

__all__ = [
    "can_approve_payroll",
    "can_post_payroll",
]
