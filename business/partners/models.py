# business/partners/models.py

from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel
from django.core.validators import MinValueValidator, MaxValueValidator

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

    search_latitude = models.FloatField(null=True, db_index=True)
    search_longitude = models.FloatField(null=True, db_index=True)

    base_price = models.DecimalField(
        max_digits=14, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        db_index=True
    )
    
    rating_avg = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    rating_count = models.PositiveIntegerField(default=0)

    meta = models.JSONField(default=dict, blank=True)


    class Meta:
        db_table = "business_partners"
        unique_together = ("tenant", "code")
        ordering = ["name"]


    def __str__(self):
        return self.name