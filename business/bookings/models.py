# business/bookings/models.py

from django.db import models

from core.models.base import TenantAwareModel, ExtensibleModel
from business.users.models import BusinessUser
from business.partners.models import Partner
from business.products.models import Product


class BookingStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PENDING_PAYMENT = "PENDING_PAYMENT", "Pending Payment"
    CONFIRMED = "CONFIRMED", "Confirmed"
    ON_GOING = "ON_GOING", "On Going"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Cancelled"
    SETTLED = "SETTLED", "Settled"


class Booking(TenantAwareModel, ExtensibleModel):
    """
    Booking = Business contract between User & Partner.
    Immutable financial snapshot once confirmed.
    """

    booking_number = models.CharField(max_length=30)

    user = models.ForeignKey(
        BusinessUser,
        on_delete=models.PROTECT,
        related_name="bookings"
    )

    partner = models.ForeignKey(
        Partner,
        on_delete=models.PROTECT,
        related_name="bookings"
    )

    # Schedule
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()

    location_address = models.TextField(blank=True, null=True)
    location_lat = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    location_lng = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)

    # Pricing Snapshot
    subtotal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    # base_price = models.DecimalField(max_digits=12, decimal_places=2)
    platform_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # partner_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(
        max_length=30,
        choices=BookingStatus.choices,
        default=BookingStatus.DRAFT
    )

    payment_status = models.CharField(
        max_length=30,
        default="UNPAID"
    )

    class Meta:
        db_table = "business_bookings"
        unique_together = ("tenant", "booking_number")
        ordering = ["-start_time"]

    def __str__(self):
        return f"{self.booking_number} - {self.user}"


class BookingItem(TenantAwareModel):
    """
    Snapshot of product/service inside booking.
    """

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField(default=1)

    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "business_booking_items"