# accounting/models/account.py

from django.db import models
import uuid
from core.models.base import TenantAwareModel


class Account(TenantAwareModel):
    """
    Chart of Accounts (COA)
    """

    ACCOUNT_TYPE_CHOICES = [
        ("asset", "Asset"),
        ("liability", "Liability"),
        ("equity", "Equity"),
        ("revenue", "Revenue"),
        ("expense", "Expense"),
    ]

    NORMAL_BALANCE_CHOICES = [
        ("debit", "Debit"),
        ("credit", "Credit"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)

    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPE_CHOICES
    )

    normal_balance = models.CharField(
        max_length=10,
        choices=NORMAL_BALANCE_CHOICES
    )

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children"
    )

    is_group = models.BooleanField(
        default=False,
        help_text="True = header/group, tidak boleh dipakai transaksi"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "accounting_accounts"
        unique_together = ("tenant", "code")
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"