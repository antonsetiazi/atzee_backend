# business/booking/models.py

from django.db import models
from django.core.exceptions import ValidationError
from core.models.base import TenantAwareModel


class BookingStatus(models.TextChoices):
    HOLD = "HOLD", "Hold"                # sementara (belum bayar / belum confirm)
    CONFIRMED = "CONFIRMED", "Confirmed"
    ONGOING = "ONGOING", "Ongoing"
    COMPLETED = "COMPLETED", "Completed"
    CANCELED = "CANCELED", "Canceled"
    EXPIRED = "EXPIRED", "Expired"      # hold lewat TTL


class Booking(TenantAwareModel):
    """
    Universal Booking Engine (SESSION-BASED)

    PRINCIPLE:
    - 1 Booking = 1 Session (time slot)
    - 1 Booking = 1 Order (optional link via order_id)
    - Booking TIDAK tahu:
        ❌ item
        ❌ harga
        ❌ payment

    Booking hanya bertanggung jawab untuk:
        ✅ resource scheduling
        ✅ time locking
        ✅ conflict prevention
    """

    # 🔗 Link ke Order (loose coupling, bukan FK)
    order_id = models.UUIDField(null=True, blank=True)

    # 🔥 RESOURCE ABSTRACTION (KUNCI)
    resource_type = models.CharField(max_length=50)
    resource_id = models.CharField(max_length=50)

    # ⏱️ SESSION TIME (core)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # ⏱️ Freeze duration saat booking dibuat (dalam menit)
    total_duration = models.IntegerField(null=True, blank=True)

    # lifecycle
    status = models.CharField(
        max_length=20,
        choices=BookingStatus.choices,
        default=BookingStatus.HOLD
    )

    # TTL untuk HOLD (anti ghost booking)
    expires_at = models.DateTimeField(null=True, blank=True)

    # extensibility
    meta = models.JSONField(default=dict, blank=True)

    # audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "business_bookings"

        indexes = [
            # 🔥 Core lookup (multi-tenant + resource)
            models.Index(fields=["tenant", "resource_type", "resource_id"]),

            # 🔥 Time range queries
            models.Index(fields=["start_time", "end_time"]),

            # 🔥 Status filtering
            models.Index(fields=["status"]),

            # 🔥 Critical query path (availability & conflict check)
            models.Index(fields=["tenant", "resource_type", "resource_id", "start_time"]),
        ]

        ordering = ["start_time"]

    # 🔒 Data integrity validation
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("end_time must be after start_time")

        # optional: ensure duration consistency
        if self.total_duration is not None:
            expected_duration = int((self.end_time - self.start_time).total_seconds() / 60)
            if self.total_duration != expected_duration:
                raise ValidationError("total_duration does not match start_time/end_time")

    # 🔒 Enforce validation on save
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.resource_type}:{self.resource_id} | {self.start_time} → {self.end_time}"