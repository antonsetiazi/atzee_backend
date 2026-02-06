# accounting/chart_of_accounts/models.py

from django.db import models
from core.models.base import TenantAwareModel


class AccountType(models.TextChoices):
    ASSET = "ASSET", "Asset"
    LIABILITY = "LIABILITY", "Liability"
    EQUITY = "EQUITY", "Equity"
    INCOME = "INCOME", "Income"
    EXPENSE = "EXPENSE", "Expense"


class ChartOfAccount(TenantAwareModel):
    """
    Chart of Account (financial invariant).
    
    This model defines accounting accounts only.
    It does NOT store balances or transactions.
    """

    code = models.CharField(
        max_length=50,
        help_text="Unique account code per tenant"
    )

    name = models.CharField(
        max_length=255
    )

    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children"
    )

    is_postable = models.BooleanField(
        default=True,
        help_text="Whether this account can be used in journal entries"
    )

    is_system = models.BooleanField(
        default=False,
        help_text="System-defined account (cannot be deleted)"
    )

    class Meta:
        db_table = "accounting_chart_of_accounts"
        unique_together = (
            "tenant",
            "code",
        )
        ordering = ["code"]


    def __str__(self) -> str:
        return f"{self.code} - {self.name}"