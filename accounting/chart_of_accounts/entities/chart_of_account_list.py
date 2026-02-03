# accounting/chart_of_accounts/entities/customer_list.py

from core.entities.contracts import BaseEntity
from accounting.chart_of_accounts.models import ChartOfAccount


class ChartOfAccountListEntity(BaseEntity):
    """
    accounting.chart_of_accounts.list entity
    """

    key = "chart_of_accounts.list"
    domain = "accounting"
    permission = "accounting.chart_of_accounts.view"

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

        qs = ChartOfAccount.objects.filter(
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
                "code": c.code,
                "name": c.name,
                "account_type": c.account_type,
                "is_active": c.is_active,
                # presentation helper
                "is_active_label": "Active" if c.is_active else "Inactive",
                "parent_id": str(c.parent_id) if c.parent_id else None,
                "parent_name": c.parent.name if c.parent else None,
            }
            for c in items
        ]

        return {
            "items": data,
            "total": total,
        }
