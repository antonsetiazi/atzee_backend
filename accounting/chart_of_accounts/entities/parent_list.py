# accounting/chart_of_accounts/entities/parent_list.py

from core.entities.contracts import BaseEntity
from accounting.chart_of_accounts.models import ChartOfAccount


class ChartOfAccountParentListEntity(BaseEntity):
    """
    accounting.chart_of_accounts.parent.list entity
    """

    key = "chart_of_accounts.parent.list"
    domain = "accounting"
    permission = "accounting.chart_of_accounts.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = ChartOfAccount.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).order_by("name")

        items = [
            {
                "value": str(c.id),
                "label": f"{c.code} - {c.name}",
            }
            for c in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
