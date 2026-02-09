# core/classifications/categories/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Category(TenantAwareModel):
    """
    Universal category / classification.
    Can be used by any domain (products, customers, assets, documents, etc).
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.PROTECT,
    )

    scope = models.CharField(
        max_length=50,
        help_text="Logical usage scope, e.g: product, customer, asset, document",
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_categories"
        unique_together = (
            ("tenant", "code"),
            ("tenant", "scope", "name"),
        )
        ordering = ["scope", "name"]

    def __str__(self):
        return f"[{self.scope}] {self.name}"
