# business/inventory/models/warehouse.py

from django.db import models
from core.models.base import TenantAwareModel


class Warehouse(TenantAwareModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    description = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        db_table = "business_inventory_warehouses"
        unique_together = ("tenant", "code")
        ordering = ["name"]

    def __str__(self):
        return self.name
    