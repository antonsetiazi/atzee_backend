# marketplace/models/order.py

from django.db import models
from core.models.base import TenantAwareModel
from core.users.models import User
from core.account.models import UserAddress

from marketplace.models.listing import PartnerListing
from business.partners.models import Partner

class FulfillmentType(models.TextChoices):
    DELIVERY = "delivery"
    ON_SITE = "on_site"
    PICKUP = "pickup"
    ONLINE = "online"


class PaymentStatus(models.TextChoices):
    UNPAID = "unpaid"
    PAID = "paid"
    FAILED = "failed"


class OrderStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"
    ON_GOING = "on_going"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Order(TenantAwareModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    selected_partner = models.ForeignKey(
        Partner,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="selected_orders"
    )
    
    partner = models.ForeignKey(
        Partner,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assigned_orders"
    )

    order_number = models.CharField(
        max_length=50,
        db_index=True
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID
    )

    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    # 🔥 LINK KE BOOKING (SESSION-BASED)
    booking_id = models.IntegerField(null=True, blank=True)

    # 🔥 NEW: Fulfillment Type
    fulfillment_type = models.CharField(
        max_length=20,
        choices=FulfillmentType.choices,
        default=FulfillmentType.ON_SITE
    )

    # 🔥 NEW: Address reference (optional)
    address = models.ForeignKey(
        UserAddress,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="orders"
    )

    # 🔥 NEW: Snapshot (immutable)
    address_snapshot = models.JSONField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    rejected_reason = models.TextField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "marketplace_orders"
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["tenant", "user"]),
            models.Index(fields=["tenant", "status"]),
            models.Index(fields=["booking_id"]),
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