# accounting/ledger/models.py

from django.db import models
from core.models.base import TenantAwareModel
from accounting.chart_of_accounts.models import ChartOfAccount
from accounting.journals.models import Journal, JournalLine


class LedgerEntry(TenantAwareModel):
    """
    Read-optimized ledger entry derived from journal lines.
    """

    journal = models.ForeignKey(
        Journal,
        on_delete=models.PROTECT,
        related_name="ledger_entries"
    )

    journal_line = models.ForeignKey(
        JournalLine,
        on_delete=models.PROTECT
    )

    account = models.ForeignKey(
        ChartOfAccount,
        on_delete=models.PROTECT
    )

    # Snapshot (historical safety)
    account_code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    account_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    entry_date = models.DateField()

    debit = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )
    
    credit = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    balance_direction = models.CharField(
        max_length=6,
        choices=[
            ("DEBIT", "Debit"),
            ("CREDIT", "Credit"),
        ],
        help_text="Denormalized for reporting performance"
    )

    class Meta:
        db_table = "accounting_ledger_entries"
        ordering = ["entry_date", "id"]
        indexes = [
            models.Index(fields=["tenant", "account", "entry_date"]),
            models.Index(fields=["tenant", "journal"]),
        ]
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(debit=0, credit__gt=0) |
                    models.Q(credit=0, debit__gt=0)
                ),
                name="ledger_debit_xor_credit"
            )
        ]

    def save(self, *args, **kwargs):
        if self.pk:
            raise ValueError("LedgerEntry is immutable")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValueError("LedgerEntry cannot be deleted")

    def __str__(self):
        return f"{self.account.code} {self.entry_date}"

