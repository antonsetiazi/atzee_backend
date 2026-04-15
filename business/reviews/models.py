# business/reviews/models.py

from django.db import models
from core.models.base import TenantAwareModel
from business.booking.models import Booking
from marketplace.models.order import Order
from business.partners.models import Partner
from core.users.models import User


class Review(TenantAwareModel):
    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="review"
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="reviews",
        db_index=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "business_reviews"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["booking", "user"],
                name="unique_review_per_booking_user"
            )
        ]

    def __str__(self):
        return f"{self.user} -> {self.partner} ({self.rating})"