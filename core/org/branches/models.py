# core/org/branches/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Branch(TenantAwareModel):
    """
    Organizational branch / office inside a tenant.
    Example: HEAD_OFFICE, JAKARTA_01, SURABAYA
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_branches"
        unique_together = ("tenant", "code")
        ordering = ["name"]

    def __str__(self):
        return self.name
