# business/customers/models.py

from django.db import models
from shared.models import TenantAwareModel


class Customer(TenantAwareModel):
    """
    Core customer model (business invariant).
    """

    code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Optional internal customer code"
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


    class Meta:
        db_table = "business_customers"
        unique_together = ("tenant", "code")
        ordering = ["name"]


    def __str__(self):
        return self.name