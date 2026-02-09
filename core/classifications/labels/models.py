# core/classifications/labels/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Label(TenantAwareModel):
    """
    Universal label / metadata.
    Can be used across multiple domains (products, customers, documents, etc).
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    scope = models.CharField(
        max_length=50,
        help_text="Logical usage scope, e.g: product, customer, document",
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_labels"
        unique_together = (
            ("tenant", "code"),
            ("tenant", "scope", "name"),
        )
        ordering = ["scope", "name"]

    def __str__(self):
        return f"[{self.scope}] {self.name}"
