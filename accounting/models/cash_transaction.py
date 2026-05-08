# accounting/models/cash_transaction.py

from django.db import models
import uuid

from core.models.base import (
    TenantAwareModel
)


class CashTransaction(
    TenantAwareModel
):

    TRANSACTION_TYPE_CHOICES = [
        ("cash_in", "Cash In"),
        ("cash_out", "Cash Out"),
        ("transfer", "Transfer"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    transaction_number = models.CharField(
        max_length=100
    )

    transaction_type = models.CharField(
        max_length=30,
        choices=TRANSACTION_TYPE_CHOICES
    )

    transaction_date = models.DateField()

    from_account = models.ForeignKey(
        "accounting.CashBankAccount",
        on_delete=models.PROTECT,
        related_name="outgoing_transactions",
        null=True,
        blank=True
    )

    to_account = models.ForeignKey(
        "accounting.CashBankAccount",
        on_delete=models.PROTECT,
        related_name="incoming_transactions",
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )

    reference = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        db_table = (
            "accounting_cash_transactions"
        )

        ordering = [
            "-transaction_date"
        ]

    def __str__(self):
        return self.transaction_number