# accounting/entities/account_select_list.py

from core.entities.contracts import BaseEntity
from accounting.models import Account
from accounting.enum.permissions import AccountingPermission


class AccountSelectListEntity(BaseEntity):
    """
    accounts.select.list entity
    """

    key = "accounting.accounts.select.list"
    domain = "accounting"
    permission = AccountingPermission.ACCOUNT_LIST_SELECT

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Account.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
            is_group=False,
        )

        scope = query.get("scope")

        if scope:
            qs = qs.filter(scope=scope)

        qs = qs.order_by("name")

        items = [
            {
                "value": str(c.id),
                "label": f"{c.code} • {c.name}"
            }
            for c in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
