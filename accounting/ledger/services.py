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
    
    entries = []

    for line in journal.lines.all():
        entries.append(
            LedgerEntry(
                tenant=journal.tenant,
                journal=journal,
                journal_line=line,
                account=line.account,
                entry_date=journal.journal_date,
                debit=line.debit,
                credit=line.credit,
                balance_direction=(
                    "DEBIT" if line.debit > 0 else "CREDIT"
                ),
                created_by=journal.updated_by
            )
        )
    
    LedgerEntry.objects.bulk_create(entries)