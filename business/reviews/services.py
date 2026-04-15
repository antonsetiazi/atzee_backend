# business/reviews/services.py

from django.db.models import F
from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError

from business.booking.models import Booking, BookingStatus
from marketplace.models.order import Order, OrderStatus
from .models import Review


@transaction.atomic
def create_review(*, tenant, user, booking_id, rating, comment=""):
    # 1. booking must exist
    booking = Booking.objects.filter(
        tenant=tenant,
        id=booking_id,
        created_by=user,
    ).first()

    if not booking:
        raise ValidationError("Booking not found.")

    # 2. booking must be completed
    if booking.status != BookingStatus.COMPLETED:
        raise ValidationError("Review only allowed for completed booking.")

    # 3. find order linked to booking
    order = Order.objects.filter(
        tenant=tenant,
        booking_id=booking.id
    ).select_related("partner").first()

    if not order:
        raise ValidationError("Order not found for this booking.")

    # 4. partner must exist
    if not order.partner:
        raise ValidationError("Partner not found.")

    # 5. prevent duplicate review
    already_exists = Review.objects.filter(
        tenant=tenant,
        booking_id=booking.id,
        user=user
    ).exists()

    if already_exists:
        raise ValidationError("You already reviewed this booking.")

    # 6. create review
    review = Review.objects.create(
        tenant=tenant,
        booking=booking,
        order=order,
        partner=order.partner,
        user=user,
        rating=rating,
        comment=comment,
        created_by=user,
        updated_by=user,
    )

    # 7. update partner aggregate rating
    partner = order.partner

    rating = Decimal(rating)

    partner.rating_avg = (
        (F("rating_avg") * F("rating_count")) + rating
    ) / (F("rating_count") + 1)
    partner.rating_count = F("rating_count") + 1

    partner.save(update_fields=["rating_avg", "rating_count"])
    partner.refresh_from_db()

    return review