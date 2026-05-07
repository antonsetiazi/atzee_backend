# accounting/entities/account_create.py

from core.entities.contracts import BaseEntity
from accounting.models import Account

from accounting.enum.permissions import AccountingPermission

class AccountCreateEntity(BaseEntity):
    key = "accounting.accounts.create"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_ACCOUNT_CREATE

    def query(self, *, user, tenant, query: dict):
        return {}
    
    def execute(self, *, user, tenant, data: dict):

        account = Account.objects.create(
            tenant=tenant,
            code=data["code"],
            name=data["name"],
            account_type=data["account_type"],
            normal_balance=data["normal_balance"],
            parent_id=data.get("parent"),
            is_group=data.get("is_group", False),
            created_by=user
        )

        return {
            "success": True,
            "id": str(account.id)
        }