# accounting/entities/account_detail.py

from core.entities.contracts import BaseEntity
from accounting.models import Account

from accounting.enum.permissions import AccountingPermission


class AccountDetailEntity(BaseEntity):
    key = "accounting.accounts.detail"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_ACCOUNT_DETAIL

    def query(self, *, user, tenant, query: dict):

        account = Account.objects.filter(
            tenant=tenant,
            id=query.get("id"),
            is_deleted=False,
        ).first()
        
        if not account:
            raise Exception("Account not found")

        return {
            "id": str(account.id),
            "code": account.code,
            "name": account.name,
            "account_type": account.account_type,
            "normal_balance": account.normal_balance,
            "parent_id": str(account.parent_id) if account.parent_id else None,
            "is_active": account.is_active,
            "is_group": account.is_group,
        }