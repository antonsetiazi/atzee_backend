# accounting/models/cash_bank_account.py

import uuid

from django.db import models

from core.models.base import TenantAwareModel


class CashBankAccount(TenantAwareModel):

    ACCOUNT_TYPE_CHOICES = [
        ("cash", "Cash"),
        ("bank", "Bank"),
        ("ewallet", "E-Wallet"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    account_type = models.CharField(
        max_length=20, choices=ACCOUNT_TYPE_CHOICES, default="bank"
    )
    bank_name = models.CharField(max_length=255, blank=True)
    bank_account_number = models.CharField(max_length=100, blank=True)
    account_holder_name = models.CharField(max_length=255, blank=True)
    accounting_account = models.ForeignKey(
        "accounting.Account",
        on_delete=models.PROTECT,
        related_name="cash_bank_accounts",
    )
    current_balance = models.DecimalField(
        max_digits=18, decimal_places=2, default=0
    )
    is_default = models.BooleanField(default=False)

    class Meta:
        db_table = "accounting_cash_bank_accounts"
        ordering = ["name"]
        unique_together = (
            "tenant",
            "code",
        )

    def __str__(self):
        return self.name
