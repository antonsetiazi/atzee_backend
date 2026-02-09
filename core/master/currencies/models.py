# core/master/currencies/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Currency(TenantAwareModel):
    """
    Currency master (ISO 4217 based).
    Example: IDR, USD, EUR
    """

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, blank=True)

    decimal_places = models.PositiveSmallIntegerField(default=2)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_currencies"
        unique_together = ("tenant", "code")
        ordering = ["code"]

    def __str__(self):
        return f"{self.code}"
