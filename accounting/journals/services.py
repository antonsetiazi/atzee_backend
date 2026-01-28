from decimal import Decimal
from django.db import transaction
from django.db import models
from django.utils import timezone

from accounting.journals.models import Journal, JournalLine
from accounting.journals.constants import JournalStatus
from accounting.journals.constants import JournalType
from accounting.journals.exceptions import (
    JournalError,
    JournalNotBalancedError,
    JournalAlreadyPostedError,
    JournalImmutableError,
    JournalAlreadyReversedError
)
from accounting.fiscal_period.selectors import get_active_period
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_journal(
    *,
    tenant: Tenant,
    created_by: User,
    journal_number: str,
    journal_type: str,
    journal_date,
    description: str = "",
    source_app: str | None = None,
    source_id: str | None = None,
) -> Journal:
    return Journal.objects.create(
        tenant=tenant,
        journal_number=journal_number,
        journal_type=journal_type,
        journal_date=journal_date,
        description=description,
        source_app=source_app,
        source_id=source_id,
        created_by=created_by
    )


def add_journal_line(
    *,
    journal: Journal,
    account,
    debit: Decimal = Decimal("0"),
    credit: Decimal = Decimal("0"),
    memo: str = "",
) -> JournalLine:
    
    if journal.status != JournalStatus.DRAFT:
        raise JournalImmutableError("Cannot modify non-draft journal.")
    
    return JournalLine.objects.create(
        journal=journal,
        account=account,
        debit=debit,
        credit=credit,
        memo=memo
    )


@transaction.atomic
def post_journal(*, journal: Journal, posted_by: User) -> Journal:

    period = get_active_period(tenant=journal.tenant)

    if not period:
        raise JournalError("No active fiscal period.")
    
    if not (period.start_date <= journal.journal_date <= period.end_date):
        raise JournalError("Journal date outside active fiscal period.")

    if journal.status != JournalStatus.DRAFT:
        raise JournalAlreadyPostedError("Journal already posted.")
    
    totals = journal.lines.aggregate(
        total_debit=models.Sum("debit"),
        total_credit=models.Sum("credit"),
    )

    if totals["total_debit"] != totals["total_credit"]:
        raise JournalNotBalancedError("Debit and credit not balanced.")

    journal.status = JournalStatus.POSTED
    journal.updated_by = posted_by
    journal.updated_at = timezone.now()
    journal.save(update_fields=[
        "status",
        "updated_by",
        "updated_at"
    ])


    # Auto-post to Ledger
    from accounting.ledger.services import post_journal_to_ledger
    post_journal_to_ledger(journal=journal)

    return journal


@transaction.atomic
def reverse_journal(
    *,
    journal: Journal,
    reversed_by: User,
    reversal_date,
    reason: str = ""
) -> Journal:
    """
    Reverse a posted journal by creating a new adjustment journal.
    """

    if journal.status != JournalStatus.POSTED:
        raise JournalImmutableError("Only posted journal can be reversed.")
    
    if journal.reversals.exists():
        raise JournalAlreadyReversedError("Journal already reversed.")
    
    # 1. Create reversal journal header
    reversal_journal = Journal.objects.create(
        tenant=journal.tenant,
        journal_number=f"REV-{journal.journal_number}",
        journal_type=JournalType.ADJUSTMENT,
        journal_date=reversal_date,
        description=reason or f"Reversal of {journal.journal_number}",
        source_app="journals",
        source_id=str(journal.id),
        status=JournalStatus.DRAFT,
        reversed_from=journal,
        created_by=reversed_by,
    )

    # 2. Reverse all lines
    for line in journal.lines.all():
        JournalLine.objects.create(
            journal=reversal_journal,
            account=line.account,
            debit=line.credit,
            credit=line.debit,
            memo=f"Reversal: {line.memo or ''}"
        )

    # 3. Post reversal journal
    post_journal(
        journal=reversal_journal,
        posted_by=reversed_by
    )

    # 4. Mark original journal as reversed
    journal.status = JournalStatus.REVERSED
    journal.updated_by = reversed_by
    journal.save(update_fields=[
        "status",
        "updated_by",
        "updated_at"
    ])

    return reversal_journal