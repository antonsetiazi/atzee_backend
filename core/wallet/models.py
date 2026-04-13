# core/wallet/models.py

from django.db import models
from django.core.exceptions import ValidationError
from core.models.base import TenantAwareModel
from core.users.models import User
from decimal import Decimal


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

    # ✅ AVAILABLE: bisa dipakai / ditarik
    available_balance = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal("0"))

    # ✅ HELD: uang escrow (belum jadi milik user)
    held_balance = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal("0"))

    class Meta:
        db_table = "core_wallets"
        indexes = [
            models.Index(fields=["tenant", "user"]),
        ]

    def __str__(self):
        return f"{self.user} | avail={self.available_balance} held={self.held_balance}"


class WalletTransactionType(models.TextChoices):
    TOPUP = "topup"
    PAYMENT = "payment"
    REFUND = "refund"
    ESCROW_HOLD = "escrow_hold"
    ESCROW_RELEASE = "escrow_release"
    ADJUSTMENT = "adjustment"


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
    
    transaction_type = models.CharField(
        max_length=50,
        choices=WalletTransactionType.choices,
    )

    # 🔗 Strong reference
    reference_type = models.CharField(max_length=50, null=True, blank=True)
    reference_id = models.CharField(max_length=100, null=True, blank=True)

    # 🔐 Idempotency (ANTI DOUBLE)
    idempotency_key = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True, default="")

    class Meta:
        db_table = "core_wallet_transactions"
        indexes = [
            models.Index(fields=["tenant", "wallet", "transaction_type"]),
            models.Index(fields=["reference_type", "reference_id"]),
        ]

    def clean(self):
        if self.amount == 0:
            raise ValidationError("Transaction amount cannot be zero.")