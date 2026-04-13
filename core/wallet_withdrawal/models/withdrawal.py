# core/wallet_withdrawal/models/withdrawal.py

from django.db import models
from decimal import Decimal
from core.models.base import TenantAwareModel
from core.users.models import User
from core.wallet.models import Wallet


class WithdrawalStatus(models.TextChoices):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Withdrawal(TenantAwareModel):
    """
    Withdrawal request dari wallet ke external account.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="withdrawals",
    )

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name="withdrawals",
    )

    amount = models.DecimalField(max_digits=18, decimal_places=2)
    fee = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal("0"))

    status = models.CharField(
        max_length=20,
        choices=WithdrawalStatus.choices,
        default=WithdrawalStatus.PENDING,
    )

    # 🔗 destination (bank / ewallet)
    destination = models.JSONField()

    # 🔗 external payout reference
    external_id = models.CharField(max_length=100, null=True, blank=True)

    processed_at = models.DateTimeField(null=True, blank=True)
    failed_reason = models.TextField(blank=True, default="")

    class Meta:
        db_table = "core_wallet_withdrawals"
        indexes = [
            models.Index(fields=["tenant", "user", "status"]),
        ]

    def __str__(self):
        return f"{self.user} | {self.amount} | {self.status}"