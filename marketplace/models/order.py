# marketplace/models/order.py

from django.db import models
from core.models.base import TenantAwareModel
from core.users.models import User

from marketplace.models.listing import PartnerListing


class OrderStatus(models.TextChoices):
    PENDING = "pending"
    PAID = "paid"
    COMPLETED = "completed"
    FAILED = "failed"


class Order(TenantAwareModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    order_number = models.CharField(
        max_length=50,
        db_index=True
    )

    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "marketplace_orders"
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["tenant", "user"]),
            models.Index(fields=["tenant", "status"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["tenant", "order_number"],
                name="unique_order_number_per_tenant"
            )
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )

    listing = models.ForeignKey(
        PartnerListing,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "marketplace_order_items"

        indexes = [
            models.Index(fields=["order"]),
        ]