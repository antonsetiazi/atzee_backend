# business/products/models.py


from django.db import models
from shared.models import TenantAwareModel


class Product(TenantAwareModel):
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