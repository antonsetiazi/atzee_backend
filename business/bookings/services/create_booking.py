import uuid
from django.db import transaction
from rest_framework.exceptions import ValidationError

from business.bookings.models import Booking, BookingStatus
from business.bookings import selectors
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

    base_price = partner.default_tariff
    platform_fee = base_price * tenant.platform_fee_percent / 100
    total_price = base_price
    partner_amount = total_price - platform_fee

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
        base_price=base_price,
        platform_fee=platform_fee,
        total_price=total_price,
        partner_amount=partner_amount,
        status=BookingStatus.PENDING_PAYMENT,
        created_by=created_by
    )

    return booking
