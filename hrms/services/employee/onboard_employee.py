# hrms/services/employee/onboard_employee.py

from django.db import transaction

from hrms.enums import EmployeeStatus
from hrms.models import Employee


@transaction.atomic
def onboard_employee(
    *,
    tenant,
    employee_id,
    full_name,
    email="",
    phone="",
    gender="",
    birth_date=None,
    department=None,
    position=None,
    manager=None,
    join_date=None,
    contract_type=None,
    employment_type=None,
    created_by=None,
):
    """
    Onboard new employee into workforce system.
    """

    employee = Employee.objects.create(
        tenant=tenant,
        employee_id=employee_id,
        full_name=full_name,
        email=email,
        phone=phone,
        gender=gender,
        birth_date=birth_date,
        department=department,
        position=position,
        manager=manager,
        join_date=join_date,
        contract_type=contract_type,
        employment_type=employment_type,
        employment_status=EmployeeStatus.ACTIVE,
        created_by=created_by,
        updated_by=created_by,
    )

    # future:
    # create activity
    # send notification
    # initialize payroll
    # create onboarding workflow

    return employee
