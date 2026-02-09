# core/org/departments/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Department(TenantAwareModel):
    """
    Organizational department inside a tenant.
    Example: FINANCE, SALES, WAREHOUSE
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="children"
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_departments"
        unique_together = ("tenant", "code")
        ordering = ["name"]

    def __str__(self):
        return self.name
