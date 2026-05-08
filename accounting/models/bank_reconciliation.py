# accounting/models/bank_reconciliation.py

from django.db import models
import uuid

from core.models.base import (
    TenantAwareModel
)


class BankReconciliation(
    TenantAwareModel
):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("completed", "Completed"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    account = models.ForeignKey(
        "accounting.CashBankAccount",
        on_delete=models.PROTECT,
        related_name="reconciliations"
    )

    start_date = models.DateField()

    end_date = models.DateField()

    statement_balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    system_balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    difference = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    notes = models.TextField(blank=True)

    class Meta:
        db_table = (
            "accounting_bank_reconciliations"
        )

        ordering = [
            "-start_date"
        ]