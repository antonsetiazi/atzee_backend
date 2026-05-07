# accounting/entities/ledger_account.py

from core.entities.contracts import BaseEntity
from accounting.models import AccountLedger

from accounting.enum.permissions import AccountingPermission


class LedgerAccountEntity(BaseEntity):
    key = "accounting.ledger.account"
    domain = "accounting"
    permission = AccountingPermission.ADMIN_ACCOUNT_VIEW

    def query(self, *, user, tenant, query: dict):

        account_id = query.get("account_id")

        qs = AccountLedger.objects.filter(
            tenant=tenant,
        )

        # 🔥 OPTIONAL FILTER
        if account_id:
            qs = qs.filter(account_id=account_id)

        qs = qs.select_related(
            "journal",
            "account",
        ).order_by("date", "created_at")

        return {
            "items": [
                {
                    "id": str(l.id),
                    "date": l.date,

                    # 🔥 ACCOUNT INFO
                    "account_code": l.account.code,
                    "account_name": l.account.name,

                    # 🔥 TAMBAHAN PENTING
                    "reference": l.journal.reference,
                    "description": l.journal.description,

                    "debit": l.debit,
                    "credit": l.credit,
                    "balance": l.balance,
                }
                for l in qs.select_related("journal")
            ]
        }