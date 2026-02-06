# business/inventory/models/lot.py

from django.db import models
from core.models.base import TenantAwareModel
from business.products.models import Product


class InventoryLot(TenantAwareModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="inventory_lots"
    )

    lot_code = models.CharField(max_length=64)

    expiry_date = models.DateField(null=True, blank=True)
    manufacture_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "business_inventory_lots"
        unique_together = ("tenant", "product", "lot_code")
        indexes = [
            models.Index(fields=["tenant", "product"]),
            models.Index(fields=["tenant", "expiry_date"]),
        ]

    def __str__(self):
        return f"{self.product} [{self.lot_code}]"
