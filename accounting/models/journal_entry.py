# accounting/models/journal_entry.py

from django.db import models
import uuid
from core.models.base import TenantAwareModel


class JournalEntry(TenantAwareModel):
    """
    Detail debit/kredit per akun
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    journal = models.ForeignKey(
        "accounting.Journal",
        on_delete=models.CASCADE,
        related_name="entries"
    )

    account = models.ForeignKey(
        "accounting.Account",
        on_delete=models.PROTECT,
        related_name="entries"
    )

    debit = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    description = models.TextField(blank=True)

    class Meta:
        db_table = "accounting_journal_entries"

    def __str__(self):
        return f"{self.account_id} | D:{self.debit} C:{self.credit}"