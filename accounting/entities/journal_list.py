# accounting/entities/journal_list.py

from core.entities.contracts import BaseEntity
from accounting.models import Journal, JournalEntry

from django.db.models import Sum

from accounting.enum.permissions import AccountingPermission


class JournalListEntity(BaseEntity):
    key = "accounting.journals.list"
    domain = "accounting"
    permission = AccountingPermission.JOURNAL_VIEW

    def query(self, *, user, tenant, query: dict):

        qs = Journal.objects.filter(
            tenant=tenant,
            is_deleted=False,
        ).order_by("-date")

        items = []

        for j in qs:
            totals = JournalEntry.objects.filter(
                journal=j
            ).aggregate(
                total_debit=Sum("debit"),
                total_credit=Sum("credit"),
            )

            items.append({
                "id": str(j.id),
                "date": j.date,
                "reference": j.reference,
                "description": j.description,
                "total_debit": totals["total_debit"] or 0,
                "total_credit": totals["total_credit"] or 0,
            })

        return {
            "items": items,
            "total": qs.count(),
        }