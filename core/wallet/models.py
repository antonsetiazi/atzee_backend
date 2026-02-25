# core/wallet/models.py

from django.db import models
from django.core.exceptions import ValidationError
from core.models.base import TenantAwareModel
from core.users.models import User


class Wallet(TenantAwareModel):
    """
    Internal wallet per user.
    Balance disimpan dalam minor currency unit (contoh: cents / IDR).
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="wallet",
    )

    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        db_table = "core_wallets"
        indexes = [
            models.Index(fields=["tenant", "user"]),
        ]

    def __str__(self):
        return f"{self.user} - {self.balance}"


class WalletTransaction(TenantAwareModel):
    """
    Ledger / transaction history for wallet.
    """

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    # credit / debit
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    # type: topup, payment, refund, adjustment
    transaction_type = models.CharField(max_length=50)
    # optional reference to domain object (booking, invoice, etc)
    reference = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, default="")

    class Meta:
        db_table = "core_wallet_transactions"
        indexes = [
            models.Index(fields=["tenant", "wallet", "transaction_type"]),
        ]

    def clean(self):
        if self.amount == 0:
            raise ValidationError("Transaction amount cannot be zero.")