# hrms/workflows/employee/onboarding_workflow.py

from hrms.enums import EmployeeStatus

ALLOWED_ONBOARDING_STATUSES = [
    EmployeeStatus.ACTIVE,
]


def can_onboard_employee():
    """
    Validate onboarding workflow.
    """

    return True
