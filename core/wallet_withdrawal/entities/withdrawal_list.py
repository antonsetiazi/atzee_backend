# core/wallet_withdrawal/entities/withdrawal_list.py

from django.utils.timezone import localtime

from core.entities.contracts import BaseEntity
from core.enum.permissions import CorePermission
from core.wallet_withdrawal.models.withdrawal import Withdrawal


class WithdrawalListEntity(BaseEntity):
    key = "withdrawals.list"
    domain = "core"
    permission = CorePermission.ADMIN_WALLET_WITHDRAWAL_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = Withdrawal.objects.filter(
            tenant=tenant,
        ).select_related("user", "wallet")

        # 🔍 SEARCH (nama / phone user)
        search = query.get("search")
        if search:
            qs = qs.filter(user__full_name__icontains=search)

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 1000))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("-id")[offset:limit]

        data = []
        for w in items:
            destination = w.destination or {}

            data.append(
                {
                    "id": str(w.id),
                    # 👤 USER
                    "user_name": w.user.full_name or w.user.username,
                    "user_phone": w.user.phone or "-",
                    # 💰 AMOUNT
                    "amount": float(w.amount),
                    "fee": float(w.fee),
                    "net_amount": float(w.amount - w.fee),
                    # 🏦 DESTINATION (simple readable)
                    "destination_label": self._format_destination(destination),
                    # 🔄 STATUS
                    "status": w.status,
                    # ⏱️ TIME
                    "processed_at": (
                        localtime(w.processed_at) if w.processed_at else None
                    ),
                }
            )

        return {
            "items": data,
            "total": total,
        }

    # 🔥 helper biar UI clean
    def _format_destination(self, dest: dict) -> str:
        """
        Example destination:
        {
            "bank_name": "BCA",
            "account_number": "123xxx",
            "account_name": "Anton"
        }
        """
        if not dest:
            return "-"

        bank = dest.get("bank_name")
        acc = dest.get("account_number")

        if bank and acc:
            return f"{bank} • {acc}"

        return str(dest)
