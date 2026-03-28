# marketplace/models/listing.py

from django.db import models
from core.models.base import TenantAwareModel

from business.partners.models import Partner
from marketplace.models.catalog import MarketplaceProduct


class PartnerListing(TenantAwareModel):
    """
    Apa yang dijual partner di marketplace
    """

    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="marketplace_listings"
    )

    product = models.ForeignKey(
        MarketplaceProduct,
        on_delete=models.CASCADE,
        related_name="listings"
    )

    price = models.DecimalField(max_digits=12, decimal_places=2)

    duration_minutes = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    stock = models.IntegerField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "marketplace_partner_listings"
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["tenant", "is_active"]),
        ]

    def __str__(self):
        return f"{self.partner} - {self.product}"