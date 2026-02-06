# business/inventory/models/stock_movement.py

from django.db import models
from core.models.base import TenantAwareModel
from business.products.models import Product
from .warehouse import Warehouse
from .lot import InventoryLot

class StockMovement(TenantAwareModel):
    IN = "IN"
    OUT = "OUT"
    ADJUST = "ADJUST"

    MOVEMENT_TYPE_CHOICES = (
        (IN, "Stock In"),
        (OUT, "Stock Out"),
        (ADJUST, "Adjustment"),
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="stock_movements"
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.PROTECT,
        related_name="stock_movements"
    )

    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=15, decimal_places=3)
    reference_type = models.CharField(max_length=50, blank=True)
    reference_id = models.PositiveIntegerField(null=True, blank=True)
    note = models.TextField(blank=True)

    lot = models.ForeignKey(
        InventoryLot,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="stock_movements"
    )
    
    class Meta:
        db_table = "business_inventory_stock_movements"
        indexes = [
            models.Index(fields=["tenant", "product"]),
            models.Index(fields=["tenant", "warehouse"]),
            models.Index(fields=["tenant", "created_at"]),
        ]


    def __str__(self):
        return f"{self.movement_type} {self.quantity} {self.product}"