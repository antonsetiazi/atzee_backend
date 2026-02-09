# core/classifications/tags/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Tag(TenantAwareModel):
    """
    Tag for classification (flat, non-hierarchical)
    Example: urgent, vip, internal
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")

    class Meta:
        db_table = "core_tags"
        unique_together = ("tenant", "code")

    def __str__(self):
        return self.name
