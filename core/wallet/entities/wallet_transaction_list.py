# core/wallet/entities/wallet_transaction_list.py

from django.db.models import Q
from django.utils.timezone import localtime

from core.entities.contracts import BaseEntity
from core.enum.permissions import CorePermission
from core.wallet.models import WalletTransaction


class WalletTransactionListEntity(BaseEntity):
    key = "wallet_transactions.list"
    domain = "core"
    permission = CorePermission.ADMIN_WALLET_TRANSACTIONS_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:

        qs = WalletTransaction.objects.filter(
            tenant=tenant,
        ).select_related("wallet__user")

        # 🔍 SEARCH (user / reference / idempotency)
        search = query.get("search")
        if search:
            qs = qs.filter(
                Q(wallet__user__full_name__icontains=search)
                | Q(wallet__user__username__icontains=search)
                | Q(reference_id__icontains=search)
                | Q(idempotency_key__icontains=search)
            )

        # 📄 PAGINATION
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 1000))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("-created_at")[offset:limit]

        data = []
        for t in items:
            user = t.wallet.user

            data.append(
                {
                    "id": str(t.id),
                    # 👤 user
                    "user_name": user.full_name or user.username,
                    "user_phone": user.phone or "-",
                    # 💳 wallet
                    "wallet_id": str(t.wallet.id),
                    # 💰 amount
                    "amount": float(t.amount),
                    # 🔄 type
                    "transaction_type": t.transaction_type,
                    # 🔗 reference
                    "reference_type": t.reference_type or "-",
                    "reference_id": t.reference_id or "-",
                    # 📝 description
                    "description": t.description or "-",
                    # 🔐 idempotency
                    "idempotency_key": t.idempotency_key,
                    # ⏱️ time
                    "created_at": localtime(t.created_at),
                }
            )

        return {
            "items": data,
            "total": total,
        }
