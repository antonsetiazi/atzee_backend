# core/schedule/recurring/entities/recurring_select_list.py

from core.entities.contracts import BaseEntity
from core.schedule.recurring.models import RecurringRule


class RecurringRuleSelectListEntity(BaseEntity):
    """
    recurring.select.list entity
    """

    key = "schedule.recurring.select.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = RecurringRule.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).order_by("name")

        items = [
            {
                "value": str(r.id),
                "label": r.name,
            }
            for r in qs
        ]

        return {"items": items, "total": qs.count()}
