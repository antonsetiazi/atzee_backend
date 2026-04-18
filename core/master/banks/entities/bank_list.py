# core/master/banks/entities/bank_list.py

from core.entities.contracts import BaseEntity
from core.master.banks.models import Bank

from core.enum.permissions import CorePermission


class BankListEntity(BaseEntity):
    key = "master.banks.list"
    domain = "core"
    permission = CorePermission.ADMIN_BANK_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = Bank.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        search = query.get("search")
        if search:
            qs = qs.filter(
                name__icontains=search
            ) | qs.filter(
                code__icontains=search
            )

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("sort_order", "name")[offset:limit]

        return {
            "items": [
                {
                    "id": str(b.id),
                    "code": b.code,
                    "name": b.name,
                    "short_name": b.short_name,
                    "sort_order": b.sort_order,
                    "is_active": b.is_active,
                    "created_at": b.created_at,
                }
                for b in items
            ],
            "total": total,
        }