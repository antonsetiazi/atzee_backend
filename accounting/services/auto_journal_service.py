# accounting/services/auto_journal_service.py

from accounting.models import JournalMapping
from accounting.services.journal_service import JournalService


class AutoJournalService:

    @staticmethod
    def create_from_transaction(
        *,
        tenant,
        user,
        transaction_type,
        reference,
        date,
        payload
    ):
        """
        payload = dict data transaksi
        contoh:
        {
            "total_amount": 1000000
        }
        """

        mappings = JournalMapping.objects.filter(
            tenant=tenant,
            transaction_type=transaction_type
        ).order_by("order")

        if not mappings:
            raise ValueError(f"No journal mapping for {transaction_type}")

        entries_data = []

        for m in mappings:
            amount = payload.get(m.amount_source)

            if amount is None:
                raise ValueError(
                    f"Missing field '{m.amount_source}' in payload"
                )

            entry = {
                "account_id": m.account.id,
                "debit": amount if m.entry_type == "debit" else 0,
                "credit": amount if m.entry_type == "credit" else 0,
                "description": transaction_type
            }

            entries_data.append(entry)

        journal = JournalService.create_journal(
            tenant=tenant,
            user=user,
            date=date,
            description=f"Auto: {transaction_type}",
            reference=reference,
            entries_data=entries_data,
            auto_post=True
        )

        return journal