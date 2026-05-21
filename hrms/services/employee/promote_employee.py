# hrms/services/employee/promote_employee.py

from django.db import transaction


@transaction.atomic
def promote_employee(
    *,
    employee,
    new_position,
    updated_by=None,
):
    """
    Promote employee into higher position.
    """

    employee.position = new_position

    employee.updated_by = updated_by

    employee.save()

    # future:
    # salary adjustment
    # promotion history
    # payroll update
    # approval workflow
    # notifications

    return employee
