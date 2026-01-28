from django.conf import settings
from django.db import models
from shared.models import TenantAwareModel


class FiscalPeriod(TenantAwareModel):
    """
    Accounting fiscal period (monthly / yearly).
    """

    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    is_closed = models.BooleanField(default=False)
    closed_at = models.DateTimeField(null=True, blank=True)
    closed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="+"
    )

    class Meta:
        db_table = "accounting_fiscal_periods"
        ordering = ["start_date"]
        unique_together = ("tenant", "start_date", "end_date")


    def __str__(self):
        return f"{self.name}"