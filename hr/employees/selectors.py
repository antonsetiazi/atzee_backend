from typing import Optional
from django.db.models import QuerySet, Q

from hr.employees.models import Employee
from core.tenants.models import Tenant


def get_employee_queryset(*, tenant: Tenant) -> QuerySet[Employee]:
    return Employee.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_employees(*, tenant: Tenant) -> QuerySet[Employee]:
    return get_employee_queryset(
        tenant=tenant
    ).order_by("full_name")


def get_employee_by_id(
    *,
    tenant: Tenant,
    employee_id: int
) -> Optional[Employee]:
    try:
        return get_employee_queryset(
            tenant=tenant
        ).get(id=employee_id)
    except Employee.DoesNotExist:
        return None
    

def search_employees(
    *,
    tenant: Tenant,
    keyword: str
) -> QuerySet[Employee]:
    return (
        get_employee_queryset(tenant=tenant)
        .filter(
            Q(full_name__icontains=keyword)
            | Q(employee_code__icontains=keyword)
            | Q(email__icontains=keyword)
        )
        .order_by("full_name")
    )


def employee_exists(
    *,
    tenant: Tenant,
    employee_id: int
) -> bool:
    return get_employee_queryset(
        tenant=tenant
    ).filter(id=employee_id).exists()