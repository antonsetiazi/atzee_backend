# accounting/services/journal_service.py

from django.db import transaction

from accounting.models import Account, Journal, JournalEntry
from accounting.services.posting_service import PostingService


class JournalService:

    @staticmethod
    @transaction.atomic
    def create_journal(
        *,
        tenant,
        user,
        date,
        description="",
        reference="",
        entries_data=[],
        auto_post=False
    ):
        """
        entries_data = [
            {
                "account_id": UUID,
                "debit": Decimal,
                "credit": Decimal,
                "description": ""
            }
        ]
        """

        if not entries_data:
            raise ValueError("Journal entries required")

        journal = Journal.objects.create(
            tenant=tenant,
            date=date,
            description=description,
            reference=reference,
            created_by=user,
        )

        entries = []

        for item in entries_data:
            account = Account.objects.get(id=item["account_id"], tenant=tenant)

            entry = JournalEntry.objects.create(
                tenant=tenant,
                journal=journal,
                account=account,
                debit=item.get("debit", 0),
                credit=item.get("credit", 0),
                description=item.get("description", ""),
            )

            entries.append(entry)

        # optional: langsung posting
        if auto_post:
            PostingService.post_journal(journal)

        return journal
