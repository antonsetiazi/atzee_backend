from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel


class Partner(TenantAwareModel, ExtensibleModel):
    """
    Core partner model (business invariant).
    """

    code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Unique partner code per tenant"
    )

    name = models.CharField(max_length=255)

    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    meta = models.JSONField(default=dict, blank=True)


    class Meta:
        db_table = "business_partners"
        unique_together = ("tenant", "code")
        ordering = ["name"]


    def __str__(self):
        return self.name