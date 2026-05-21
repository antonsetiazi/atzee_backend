# hrms/workflows/employee/termination_workflow.py

from hrms.enums import EmployeeStatus


def can_terminate_employee(
    *,
    employee,
):
    """
    Validate employee termination workflow.
    """

    if employee.employment_status == (EmployeeStatus.TERMINATED):
        return False

    return True
