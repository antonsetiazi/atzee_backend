# core/classifications/attributes/models.py

from django.db import models
from core.models.base import TenantAwareModel


class Attribute(TenantAwareModel):
    """
    Universal attribute definition.
    Example: color, size, weight, expiry_date
    """

    TYPE_TEXT = "text"
    TYPE_NUMBER = "number"
    TYPE_BOOLEAN = "boolean"
    TYPE_DATE = "date"
    TYPE_SELECT = "select"
    TYPE_MULTI_SELECT = "multi_select"

    TYPE_CHOICES = [
        (TYPE_TEXT, "Text"),
        (TYPE_NUMBER, "Number"),
        (TYPE_BOOLEAN, "Boolean"),
        (TYPE_DATE, "Date"),
        (TYPE_SELECT, "Select"),
        (TYPE_MULTI_SELECT, "Multi Select"),
    ]

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )

    scope = models.CharField(
        max_length=50,
        help_text="Logical usage scope, e.g: product, asset, employee",
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "core_attributes"
        unique_together = (
            ("tenant", "code"),
            ("tenant", "scope", "name"),
        )
        ordering = ["scope", "name"]

    def __str__(self):
        return f"[{self.scope}] {self.name}"

