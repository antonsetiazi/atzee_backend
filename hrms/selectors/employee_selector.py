# hrms/selectors/employee_selector.py

from django.db.models import Count

from hrms.enums import EmployeeStatus
from hrms.models import Employee


def get_employee_by_id(employee_id):
    return (
        Employee.objects.filter(
            pk=employee_id,
            is_deleted=False,
        )
        .select_related(
            "department",
            "position",
            "manager",
            "user",
        )
        .first()
    )


def get_employee_by_employee_code(
    tenant,
    employee_code,
):
    return (
        Employee.objects.filter(
            tenant=tenant,
            employee_id=employee_code,
            is_deleted=False,
        )
        .select_related(
            "department",
            "position",
        )
        .first()
    )


def get_active_employees(tenant):
    return Employee.objects.filter(
        tenant=tenant,
        employment_status=EmployeeStatus.ACTIVE,
        is_deleted=False,
    ).select_related(
        "department",
        "position",
    )


def get_department_employees(
    tenant,
    department_id,
):
    return Employee.objects.filter(
        tenant=tenant,
        department_id=department_id,
        is_deleted=False,
    ).select_related(
        "position",
    )


def get_manager_subordinates(
    tenant,
    manager_id,
):
    return Employee.objects.filter(
        tenant=tenant,
        manager_id=manager_id,
        is_deleted=False,
    ).select_related(
        "department",
        "position",
    )


def get_employee_headcount_summary(
    tenant,
):
    return (
        Employee.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )
        .values(
            "employment_status",
        )
        .annotate(total=Count("id"))
    )
