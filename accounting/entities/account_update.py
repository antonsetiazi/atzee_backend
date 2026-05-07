# accounting/entities/account_update.py

from core.entities.contracts import BaseEntity
from accounting.models import Account

from accounting.enum.permissions import AccountingPermission


class AccountUpdateEntity(BaseEntity):
    key="accounting.accounts.update"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_ACCOUNT_EDIT

    def query(self, *, user, tenant, query: dict):
        return {}

    def execute(self, *, user, tenant, data: dict):
        account = Account.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).get(id=data["id"])

        if not account:
            raise Exception("Account not found")

        account.code = data["code"]
        account.name = data["name"]
        account.is_active = data["is_active"]
        account.updated_by = user
        account.save(update_fields=["code", "name", "is_active", "updated_by", "updated_at"])

        return {
            "success": True,
            "message": "Account berhasil dibuat",
            "id": str(account.id),
        }