# accounting/entities/account_list.py

from core.entities.contracts import BaseEntity
from accounting.models import Account

from accounting.enum.permissions import AccountingPermission

class AccountListEntity(BaseEntity):
    key = "accounting.accounts.list"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_ACCOUNT_VIEW

    def query(self, *, user, tenant, query: dict):

        qs = Account.objects.filter(
            tenant=tenant,
            is_deleted=False
        )

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        items = qs.order_by("code")

        return {
            "items": [
                {
                    "id": str(a.id),
                    "code": a.code,
                    "name": a.name,
                    "account_type": a.account_type,
                    "parent_name": a.parent.name if a.parent else "-",
                    "is_group": a.is_group,
                    "is_active": a.is_active,
                }
                for a in items
            ],
            "total": qs.count(),
        }