# accounting/models/ledger.py

from django.db import models
import uuid
from core.models.base import TenantAwareModel


class AccountLedger(TenantAwareModel):
    """
    Menyimpan mutasi per akun (hasil posting journal)
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    journal = models.ForeignKey(
        "accounting.Journal",
        on_delete=models.CASCADE,
        related_name="ledgers"
    )

    entry = models.ForeignKey(
        "accounting.JournalEntry",
        on_delete=models.CASCADE,
        related_name="ledgers"
    )

    account = models.ForeignKey(
        "accounting.Account",
        on_delete=models.PROTECT,
        related_name="ledgers"
    )

    date = models.DateField()

    debit = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        help_text="Running balance setelah transaksi ini"
    )

    class Meta:
        db_table = "accounting_account_ledgers"
        ordering = ["date", "created_at"]