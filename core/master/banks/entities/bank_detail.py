# core/master/banks/entities/bank_detail.py

from core.entities.contracts import BaseEntity
from core.master.banks.models import Bank

from core.enum.permissions import CorePermission


class BankDetailEntity(BaseEntity):
    key = "master.banks.detail"
    domain = "core"
    permission = CorePermission.ADMIN_BANK_EDIT

    def query(self, *, user, tenant, query: dict) -> dict:

        bank_id = query.get("id")

        bank = Bank.objects.filter(
            tenant=tenant,
            id=bank_id,
            is_deleted=False,
        ).first()

        if not bank:
            raise Exception("Bank not found")

        return {
            "id": str(bank.id),
            "code": bank.code,
            "name": bank.name,
            "short_name": bank.short_name,
            "sort_order": bank.sort_order,
            "is_active": bank.is_active,
        }