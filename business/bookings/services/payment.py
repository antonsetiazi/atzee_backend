# business/bookings/services/payment.py

from decimal import Decimal
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from core.tenants.models import Tenant
from core.wallet.services import debit_wallet
from business.bookings.models import Booking, BookingStatus
from core.wallet.models import Wallet


def pay_booking_with_wallet(*, tenant: Tenant, user, booking_id: int):
    # 1️⃣ Ambil booking berdasarkan tenant (WAJIB multi-tenant safe)
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        tenant=tenant
    )

    # 2️⃣ Validasi status
    if booking.status != BookingStatus.PENDING_PAYMENT:
        raise ValidationError("Booking is not in payable state.")

    total_amount = Decimal(booking.total_price)

    wallet = Wallet.objects.get(
        tenant=tenant,
        user=user
    )

    # 3️⃣ Debit wallet
    debit_wallet(
        tenant=tenant,
        wallet=wallet,
        amount=total_amount,
        transaction_type="BOOKING_PAYMENT",
        description="Payment for booking",
        reference=f"BOOKING-{booking.booking_number}",
    )

    # 4️⃣ Update booking status
    booking.status = BookingStatus.CONFIRMED
    booking.save(update_fields=["status", "updated_at"])

    return {
        "success": True,
        "message": "Booking successfully paid using wallet.",
        "booking_id": booking.id,
        "booking_number": booking.booking_number,
    }