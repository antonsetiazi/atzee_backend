# core/master/banks/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Bank(TenantAwareModel):
    """
    Universal tenant-aware bank master.
    Used for withdrawals, deposits, payouts, etc.
    """

    code = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50, blank=True)

    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        db_table = "core_banks"
        unique_together = (
            ("tenant", "code"),
            ("tenant", "name"),
        )
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name