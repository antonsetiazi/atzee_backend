# core/classifications/attributes/models.py

from django.db import models
from core.models.base import TenantAwareModel
from .attribute import Attribute


class AttributeOption(TenantAwareModel):
    """
    Option for select / multi_select attribute.
    """

    attribute = models.ForeignKey(
        Attribute,
        related_name="options",
        on_delete=models.CASCADE,
    )

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_attribute_options"
        unique_together = (
            ("attribute", "code"),
            ("attribute", "name"),
        )
        ordering = ["name"]

    def __str__(self):
        return f"{self.attribute.code}: {self.name}"
