# core/master/currencies/entities/currency_select_list.py

from core.entities.contracts import BaseEntity
from core.master.currencies.models import Currency


class CurrencySelectListEntity(BaseEntity):
    """
    currencies.select.list entity
    """

    key = "currencies.select.list"
    domain = "core"
    permission = "core.currencies.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Currency.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).order_by("code")

        items = [
            {
                "value": str(c.id),
                "label": f"{c.code} — {c.name}",
            }
            for c in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
