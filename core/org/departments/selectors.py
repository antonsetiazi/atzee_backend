# core/org/departments/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.org.departments.models import Department
from core.tenants.models import Tenant


def get_department_queryset(*, tenant: Tenant) -> QuerySet[Department]:
    return Department.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True
    )


def get_departments(*, tenant: Tenant) -> QuerySet[Department]:
    return get_department_queryset(tenant=tenant).select_related(
        "parent"
    ).order_by("name")


def get_department_by_id(
    *, tenant: Tenant, department_id: int
) -> Optional[Department]:
    try:
        return get_department_queryset(
            tenant=tenant
        ).get(id=department_id)
    except Department.DoesNotExist:
        return None
