# business/products/models.py


from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel


class Product(TenantAwareModel, ExtensibleModel):
    """
    Core product / service definition (business invariant).
    """

    TYPE_GOOD = "good"
    TYPE_SERVICE = "service"

    PRODUCT_TYPE_CHOICES = [
        (TYPE_GOOD, "Good"),
        (TYPE_SERVICE, "Service"),
    ]

    code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Internal product code / SKU"
    )

    name = models.CharField(max_length=255)

    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPE_CHOICES,
        default=TYPE_GOOD,
        db_index=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True, db_index=True)
    

    class Meta:
        db_table = "business_products"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["tenant", "product_type"]),
            models.Index(fields=["tenant", "is_active"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["tenant", "code"],
                name="unique_product_code_per_tenant",
                condition=~models.Q(code=None)
            )
        ]


    def __str__(self):
        return self.name
    

class PartnerOffering(TenantAwareModel):
    """
    Partner-specific offering (price, duration, availability).
    """
    partner = models.ForeignKey(
        "business_partners.Partner",
        on_delete=models.CASCADE,
        related_name="offerings"
    )

    product = models.ForeignKey(
        "business_products.Product",
        on_delete=models.CASCADE,
        related_name="offerings"
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    duration_minutes = models.PositiveIntegerField(
        default=60
    )

    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        db_table = "business_partner_offerings"
        unique_together = ("tenant", "partner", "product")
        indexes = [
            models.Index(fields=["tenant", "partner"]),
            models.Index(fields=["tenant", "is_active"]),
        ]