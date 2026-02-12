# core/schedule/recurring/entities/recurring_list.py

from core.entities.contracts import BaseEntity
from core.schedule.recurring.models import RecurringRule


class RecurringRuleListEntity(BaseEntity):
    """
    recurring.list entity
    """

    key = "schedule.recurring.list"
    domain = "core"
    permission = "core.schedule.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = RecurringRule.objects.filter(tenant=tenant, is_deleted=False)

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        qs = qs.order_by("name")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))
        offset = (page - 1) * page_size
        limit = offset + page_size
        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(r.id),
                "name": r.name,
                "frequency": r.frequency,
                "interval": r.interval,
                "start_datetime": r.start_datetime,
                "end_datetime": r.end_datetime,
            }
            for r in items
        ]
        return {"items": data, "total": total}
