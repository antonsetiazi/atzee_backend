from django.db import models
from shared.models import TenantAwareModel
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
        ]
    )

    class Meta:
        db_table = "accounting_ledger_entries"
        ordering = ["entry_date", "id"]
        indexes = [
            models.Index(fields=["tenant", "account", "entry_date"]),
        ]

    def __str__(self):
        return f"{self.account.code} {self.entry_date}"

