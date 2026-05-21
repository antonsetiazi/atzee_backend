# hrms/services/employee/transfer_employee.py

from django.db import transaction


@transaction.atomic
def transfer_employee(
    *,
    employee,
    new_department=None,
    new_position=None,
    new_manager=None,
    updated_by=None,
):
    """
    Transfer employee into new organization structure.
    """

    if new_department:
        employee.department = new_department

    if new_position:
        employee.position = new_position

    if new_manager:
        employee.manager = new_manager

    employee.updated_by = updated_by

    employee.save()

    # future:
    # create transfer history
    # create activity log
    # notify stakeholders

    return employee
