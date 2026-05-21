# hrms/workflows/employee/__init__.py

from .onboarding_workflow import (
    can_onboard_employee,
)
from .promotion_workflow import (
    can_promote_employee,
)
from .termination_workflow import (
    can_terminate_employee,
)

__all__ = [
    "can_onboard_employee",
    "can_promote_employee",
    "can_terminate_employee",
]
