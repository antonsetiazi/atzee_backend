# hrms/services/employee/terminate_employee.py

from django.db import transaction
from django.utils import timezone

from hrms.enums import EmployeeStatus


@transaction.atomic
def terminate_employee(
    *,
    employee,
    updated_by=None,
):
    """
    Terminate employee employment.
    """

    employee.employment_status = EmployeeStatus.TERMINATED
    employee.is_active = False
    employee.updated_by = updated_by
    employee.updated_at = timezone.now()
    employee.save()

    # future:
    # revoke access
    # stop payroll
    # asset return workflow
    # exit clearance
    # activity log

    return employee
