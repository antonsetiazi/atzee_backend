# accounting/entities/journal_detail.py

from django.db.models import Sum
from core.entities.contracts import BaseEntity
from accounting.models import Journal, JournalEntry

from accounting.enum.permissions import AccountingPermission


class JournalDetailEntity(BaseEntity):
    key = "accounting.journals.detail"
    domain = "accounting"
    permission = AccountingPermission.JOURNAL_VIEW

    def query(self, *, user, tenant, query: dict):
        journal = Journal.objects.get(
            tenant=tenant,
            id=query.get("id"),
            is_deleted=False,
        )

        if not journal:
            raise Exception("Journal not found")
    
        lines = JournalEntry.objects.filter(journal=journal)

        # 🔥 HITUNG TOTAL
        totals = lines.aggregate(
            total_debit=Sum("debit"),
            total_credit=Sum("credit"),
        )

        return {
            "id": str(journal.id),
            "date": journal.date,
            "reference": journal.reference,
            "description": journal.description,
            "total_debit": totals["total_debit"] or 0,
            "total_credit": totals["total_credit"] or 0,

            "lines": [
                {
                    "id": str(l.id),
                    "account_name": l.account.name,
                    "debit": l.debit,
                    "credit": l.credit,
                }
                for l in lines
            ]
        }