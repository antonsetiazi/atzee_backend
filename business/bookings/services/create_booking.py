# business/bookings/services/create_booking.py

import uuid
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta
from django.db import transaction
from rest_framework.exceptions import ValidationError

from business.bookings.models import Booking, BookingItem, BookingStatus
from business.bookings import selectors
from business.products.models import Product
from business.partners.models import Partner
from core.tenants.models import Tenant
from core.users.models import User


def _generate_booking_number() -> str:
    return f"BK-{uuid.uuid4().hex[:8].upper()}"


@transaction.atomic
def create_booking(
    *,
    tenant: Tenant,
    created_by: User,
    user,
    partner: Partner,
    start_time,
    end_time,
    items: list,  # [{product_id, quantity}]
    location_address=None,
    location_lat=None,
    location_lng=None,
) -> Booking:

    if end_time <= start_time:
        raise ValidationError("End time must be after start time.")

    # Availability validation
    overlapping = selectors.get_partner_active_bookings(
        tenant=tenant,
        partner_id=partner.id,
        start_time=start_time,
        end_time=end_time
    )

    if overlapping.exists():
        raise ValidationError("Partner not available at selected time.")

    duration_minutes = int((end_time - start_time).total_seconds() / 60)

    subtotal = Decimal("0.00")

    booking = Booking.objects.create(
        tenant=tenant,
        booking_number=_generate_booking_number(),
        user=user,
        partner=partner,
        start_time=start_time,
        end_time=end_time,
        duration_minutes=duration_minutes,
        location_address=location_address,
        location_lat=location_lat,
        location_lng=location_lng,
        subtotal_amount=0,
        # base_price=base_price,
        platform_fee=0,
        total_price=0,
        # partner_amount=partner_amount,
        status=BookingStatus.PENDING_PAYMENT,
        payment_expired_at=timezone.now() + timedelta(minutes=15),
        created_by=created_by
    )

    for item in items:
        product = Product.objects.get(id=item["product_id"], tenant=tenant)

        quantity = item.get("quantity", 1)
        unit_price = Decimal(item.get("unit_price") or product.extensions.get("price", 0))
        item_subtotal = Decimal(item.get("subtotal") or (unit_price * quantity))

        BookingItem.objects.create(
            tenant=tenant,
            booking=booking,
            product=product,
            quantity=quantity,
            unit_price=unit_price,
            subtotal=item_subtotal
        )

        subtotal += item_subtotal

    platform_fee = subtotal * Decimal(tenant.platform_fee_percent) / Decimal(100)
    total_price = subtotal + platform_fee

    booking.subtotal_amount = subtotal
    booking.platform_fee = platform_fee
    booking.total_price = total_price
    booking.save(update_fields=[
        "subtotal_amount",
        "platform_fee",
        "total_price",
        "updated_at"
    ])

    return booking
