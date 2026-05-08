# accounting/models/journal_mapping.py

from django.db import models
import uuid
from core.models.base import TenantAwareModel


class JournalMapping(TenantAwareModel):
    """
    Mapping rule untuk auto journal
    """

    TRANSACTION_TYPE_CHOICES = [
        ("sales_invoice", "Sales Invoice"),
        ("purchase_invoice", "Purchase Invoice"),
        ("payment_in", "Payment In"),
        ("payment_out", "Payment Out"),
        ("expense", "Expense"),
    ]

    ENTRY_TYPE_CHOICES = [
        ("debit", "Debit"),
        ("credit", "Credit"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    transaction_type = models.CharField(
        max_length=50,
        choices=TRANSACTION_TYPE_CHOICES
    )

    account = models.ForeignKey(
        "accounting.Account",
        on_delete=models.PROTECT
    )

    entry_type = models.CharField(
        max_length=10,
        choices=ENTRY_TYPE_CHOICES
    )

    amount_source = models.CharField(
        max_length=50,
        help_text=(
            "Field dari payload. "
            "Contoh: subtotal, tax_amount, total_amount"
        )
    )

    order = models.IntegerField(default=0)

    class Meta:
        db_table = "accounting_journal_mappings"
        ordering = ["transaction_type", "order"]