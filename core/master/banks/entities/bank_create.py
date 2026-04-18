# core/master/banks/entities/bank_create.py

from core.entities.contracts import BaseEntity
from core.master.banks import services

from core.enum.permissions import CorePermission


class BankCreateEntity(BaseEntity):
    key = "master.banks.create"
    domain = "core"
    permission = CorePermission.ADMIN_BANK_CREATE

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:

        bank = services.create_bank(
            tenant=tenant,
            created_by=user,
            code=data["code"],
            name=data["name"],
            short_name=data.get("short_name", ""),
        )

        return {
            "success": True,
            "message": "Bank berhasil dibuat",
            "id": str(bank.id),
        }