# accounting/taxes/models/tax_journal_map.py

from django.db import models
from core.models.base import TenantAwareModel
from accounting.chart_of_accounts.models import ChartOfAccount
from .tax import Tax


class TaxJournalMap(TenantAwareModel):
    """
    Defines how tax affects accounting journals.
    """

    tax = models.ForeignKey(
        Tax,
        on_delete=models.CASCADE,
        related_name="journal_maps"
    )

    JOURNAL_TYPE_CHOICES = (
        ("sales", "Sales"),
        ("purchase", "Purchase"),
    )
    journal_type = models.CharField(
        max_length=20,
        choices=JOURNAL_TYPE_CHOICES
    )

    debit_account = models.ForeignKey(
        ChartOfAccount,
        on_delete=models.PROTECT,
        related_name="+"
    )

    credit_account = models.ForeignKey(
        ChartOfAccount,
        on_delete=models.PROTECT,
        related_name="+"
    )

    class Meta:
        db_table = "accounting_tax_journal_map"
        unique_together = ("tenant", "tax", "journal_type")

    def __str__(self):
        return f"{self.tax.code} [{self.journal_type}]"
