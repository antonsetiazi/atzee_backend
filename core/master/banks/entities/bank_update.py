# core/master/banks/entities/bank_update.py

from core.entities.contracts import BaseEntity
from core.master.banks import services

from core.enum.permissions import CorePermission


class BankUpdateEntity(BaseEntity):
    key = "master.banks.update"
    domain = "core"
    permission = CorePermission.ADMIN_BANK_EDIT

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:

        bank = services.update_bank(
            tenant=tenant,
            bank_id=data["id"],
            updated_by=user,
            code=data.get("code"),
            name=data.get("name"),
            short_name=data.get("short_name"),
            sort_order=data.get("sort_order"),
            is_active=data.get("is_active"),
        )

        return {
            "success": True,
            "message": "Bank berhasil diperbarui",
            "id": str(bank.id),
        }