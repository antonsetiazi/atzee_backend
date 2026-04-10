# marketplace/models/catalog.py

from django.db import models
from core.models.base import TenantAwareModel
from core.classifications.categories.models import Category

class MarketplaceProduct(TenantAwareModel):
    """
    Catalog global (apa yang bisa dijual di marketplace)
    """

    TYPE_PRODUCT = "product"
    TYPE_SERVICE = "service"

    TYPE_CHOICES = [
        (TYPE_PRODUCT, "Product"),
        (TYPE_SERVICE, "Service"),
    ]

    partner = models.ForeignKey(
        "business_partners.Partner",
        on_delete=models.CASCADE,
        related_name="marketplace_products"
    )

    code = models.CharField(max_length=100)

    name = models.CharField(max_length=255)

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="marketplace_products"
    )

    is_active = models.BooleanField(default=True)


    class Meta:
        db_table = "marketplace_products"
        unique_together = ("partner", "code")
        ordering = ["name"]

        indexes = [
            models.Index(fields=["tenant", "is_active"]),
            models.Index(fields=["tenant", "partner"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["tenant", "partner", "name"],
                name="unique_product_per_partner"
            )
        ]

        
    def __str__(self):
        return self.name