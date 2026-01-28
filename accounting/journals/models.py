from django.db import models
from shared.models import TenantAwareModel
from accounting.chart_of_accounts.models import ChartOfAccount
from accounting.journals.constants import JournalType, JournalStatus


class Journal(TenantAwareModel):
    """
    Journal header (financial event).
    """

    journal_number = models.CharField(
        max_length=50,
        unique=True
    )

    journal_type = models.CharField(
        max_length=20,
        choices=JournalType.CHOICES
    )

    journal_date = models.DateField()

    description = models.TextField(
        blank=True,
        null=True
    )

    source_app = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Origin module (transactions, payroll, inventory, etc)"
    )

    source_id = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        help_text="UUID / ID from source module"
    )

    status = models.CharField(
        max_length=20,
        choices=JournalStatus.CHOICES,
        default=JournalStatus.DRAFT
    )

    reversed_from = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="reversals"
    )

    class Meta:
        db_table = "accounting_journals"
        ordering = ["-journal_date", "-id"]

    def __str__(self):
        return f"{self.journal_number} ({self.journal_type})"
    

class JournalLine(models.Model):
    """
    Journal line (double-entry fact).
    """

    journal = models.ForeignKey(
        Journal,
        related_name="lines",
        on_delete=models.CASCADE
    )

    account = models.ForeignKey(
        ChartOfAccount,
        on_delete=models.PROTECT
    )

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

    memo = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )


    class Meta:
        db_table = "accounting_journal_lines"

    
    def __str__(self):
        return f"{self.account.code} D:{self.debit} C:{self.credit}"