# business/inventory/models/stock_item.py

from django.db import models
from core.models.base import TenantAwareModel
from business.products.models import Product
from .warehouse import Warehouse


class StockItem(TenantAwareModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="stock_items"
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="stock_items"
    )

    quantity = models.DecimalField(
        max_digits=15,
        decimal_places=3,
        default=0
    )

    class Meta:
        db_table = "business_inventory_stock_items"
        unique_together = ("tenant", "product", "warehouse")        

    def __str__(self):
        return f"{self.product} @ {self.warehouse}"
