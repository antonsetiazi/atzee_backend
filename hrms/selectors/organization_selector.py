# hrms/selectors/organization_selector.py

from core.org.departments.models import Department


def get_active_departments(
    tenant,
):
    return Department.objects.filter(
        tenant=tenant,
        is_active=True,
        is_deleted=False,
    )


def get_department_tree(
    tenant,
):
    return Department.objects.filter(
        tenant=tenant,
        is_deleted=False,
    ).select_related(
        "parent",
    )
