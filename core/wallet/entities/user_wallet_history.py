# core/wallet/entities/user_wallet_history.py

from core.entities.contracts import BaseEntity
from core.wallet.models import WalletTransaction
from core.wallet.selectors import get_wallet


class UserWalletHistoryEntity(BaseEntity):
    """
    core.user.wallet.history
    Return:
        {
            "balance": "...",
            "items": [...],
            "total": int
        }
    """

    key = "user.wallet.history"
    domain = "core"
    permission = "core.user.wallet.view"

    def query(self, *, user, tenant, query: dict) -> dict:

        wallet = get_wallet(tenant=tenant, user=user)

        if not wallet:
            return {
                "balance": "0",
                "items": [],
                "total": 0,
            }

        qs = WalletTransaction.objects.filter(
            tenant=tenant,
            wallet=wallet,
            is_deleted=False,
        )

        # -----------------------------
        # FILTER (transaction_type)
        # -----------------------------
        trx_type = query.get("type")
        if trx_type:
            qs = qs.filter(transaction_type=trx_type)

        # -----------------------------
        # PAGINATION
        # -----------------------------
        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 1000))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()

        items = qs.order_by("-created_at")[offset:limit]

        # -----------------------------
        # SERIALIZE
        # -----------------------------
        data = [
            {
                "id": str(t.id),
                "transaction_type": t.transaction_type,
                "reference": t.reference,
                "description": t.description,
                "amount": str(t.amount),
                "created_at": t.created_at.isoformat(),
            }
            for t in items
        ]

        return {
            "balance": str(wallet.balance),
            "items": data,
            "total": total,
        }
