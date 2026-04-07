# business/tracking/models.py

from django.db import models
from core.models.base import TenantAwareModel
from business.partners.models import Partner
from marketplace.models.order import Order


class PartnerLocation(TenantAwareModel):
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="locations"
    )

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    accuracy = models.FloatField(null=True, blank=True)

    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tracking_partner_locations"

        indexes = [
            models.Index(fields=["tenant", "partner", "-recorded_at"]),
        ]


class OrderTracking(TenantAwareModel):
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="tracking"
    )

    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="order_trackings"
    )

    is_active = models.BooleanField(default=True)

    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "tracking_order_tracking"

        indexes = [
            models.Index(fields=["tenant", "partner"]),
        ]        