# hrms/workflows/employee/promotion_workflow.py


def can_promote_employee(
    *,
    employee,
):
    """
    Validate employee promotion workflow.
    """

    if not employee.is_active:
        return False

    return True
