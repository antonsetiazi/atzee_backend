from django.db import models
from shared.models import TenantAwareModel
from accounting.chart_of_accounts.models import ChartOfAccount


class Tax(TenantAwareModel):
    """
    Tax master definition (e.g. PPN 11%).
    """

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Percentage, e.g. 11.00"
    )

    is_active = models.BooleanField(default=True)

    sales_account = models.ForeignKey(
        ChartOfAccount,
        on_delete=models.PROTECT,
        related_name="+"
    )

    purchase_account = models.ForeignKey(
        ChartOfAccount,
        on_delete=models.PROTECT,
        related_name="+"
    )

    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "accounting_taxes"
        unique_together = ("tenant", "code", "effective_from")