# core/org/departments/entities/department_select_list.py

from core.entities.contracts import BaseEntity
from core.org.departments.models import Department


class DepartmentSelectListEntity(BaseEntity):
    """
    departments.select.list entity
    """

    key = "departments.select.list"
    domain = "core"
    permission = "core.departments.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Department.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).order_by("name")

        items = [
            {
                "value": str(d.id),
                "label": d.name,
            }
            for d in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
