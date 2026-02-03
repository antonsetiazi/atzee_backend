# hr/employees/entities/customer_list.py

from core.entities.contracts import BaseEntity
from hr.employees.models import Employee


class EmployeeListEntity(BaseEntity):
    """
    hr.employees.list entity
    """

    key = "employees.list"
    domain = "hr"
    permission = "hr.employees.view"

    def query(self, *, user, tenant, query: dict) -> dict:

        """
        query format (from frontend):
        {
            page: 1,
            pageSize: 10,
            search?: str,
            filters?: {},
            sort?: {}
        }
        """

        qs = Employee.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        # 🔍 SEARCH
        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()

        items = qs[offset:limit]
 
        # 🔁 SERIALIZE (simple & explicit)

        data = [            
            {
                "id": str(c.id),
                "employee_code": c.employee_code,
                "full_name": c.full_name,
                "phone": c.phone,
                "email": c.email,
                "is_active": c.is_active,
                # presentation helper
                "is_active_label": "Active" if c.is_active else "Inactive",
            }
            for c in items
        ]

        return {
            "items": data,
            "total": total,
        }
