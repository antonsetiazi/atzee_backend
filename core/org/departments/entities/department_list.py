# core/org/departments/entities/department_list.py

from core.entities.contracts import BaseEntity
from core.org.departments.models import Department


class DepartmentListEntity(BaseEntity):
    """
    departments.list entity
    """

    key = "departments.list"
    domain = "core"
    permission = "core.departments.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Department.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).select_related("parent")

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(d.id),
                "code": d.code,
                "name": d.name,
                "parent": d.parent.name if d.parent else None,
            }
            for d in items
        ]

        return {
            "items": data,
            "total": total,
        }
