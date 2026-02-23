# business/products/models.py


from django.db import models
from core.models.base import TenantAwareModel, ExtensibleModel


class Product(TenantAwareModel, ExtensibleModel):
    """
    Core product / service model (business invariant).
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
        default=TYPE_GOOD
    )

    description = models.TextField(
        blank=True,
        null=True
    )
    

    class Meta:
        db_table = "business_products"
        unique_together = ("tenant", "code")
        ordering = ["name"]


    def __str__(self):
        return self.name
    

class PartnerProduct(TenantAwareModel):
    partner = models.ForeignKey(
        "business_partners.Partner",
        on_delete=models.CASCADE,
        related_name="partner_products"
    )

    product = models.ForeignKey(
        "business_product.Product",
        on_delete=models.CASCADE,
        related_name="partner_products"
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    duration_minutes = models.PositiveIntegerField(
        default=60
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("tenant", "partner", "product")