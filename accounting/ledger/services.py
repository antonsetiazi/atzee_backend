# accounting/ledger/services.py

from django.db import transaction
from accounting.ledger.models import LedgerEntry
from accounting.journals.models import Journal
from accounting.journals.constants import JournalStatus


@transaction.atomic
def post_journal_to_ledger(*, journal: Journal) -> None:
    """
    Create ledger entries from posted journal.
    """

    if journal.status != JournalStatus.POSTED:
        return
    
    # Prevent double posting
    if journal.ledger_entries.exists():
        return
    
    lines = list(journal.lines.all())
    if not lines:
        return         # or raise error, choose one policy

    entries = []

    for line in lines:
        if line.debit > 0:
            balance = "DEBIT"
        elif line.credit > 0:
            balance = "CREDIT"
        else:
            continue  # safeguard, should not happen

        entries.append(
            LedgerEntry(
                tenant=journal.tenant,
                journal=journal,
                journal_line=line,
                account=line.account,
                account_code=line.account.code,
                account_name=line.account.name,
                entry_date=journal.journal_date,
                debit=line.debit,
                credit=line.credit,
                balance_direction=balance,
                created_by=journal.updated_by
            )
        )
    
    if entries:
        LedgerEntry.objects.bulk_create(entries)