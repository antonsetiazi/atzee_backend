# core/master/locations/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Location(TenantAwareModel):
    """
    Generic physical or logical location.

    Examples:
    - Head Office
    - Branch A
    - Room 101
    - Shelf A1
    - Virtual Location (e.g. TRANSIT)
    """

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
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
        db_table = "core_locations"
        unique_together = ("tenant", "code")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
