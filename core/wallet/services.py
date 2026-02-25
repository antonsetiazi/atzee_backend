# core/wallet/services.py

# from decimal import Decimal
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.wallet.models import Wallet, WalletTransaction
from core.tenants.models import Tenant
# from core.users.models import User

# Untuk akses booking
# from business.bookings.models import Booking


@transaction.atomic
def credit_wallet(*, tenant: Tenant, wallet: Wallet, amount: float, transaction_type: str,
                  description: str = "", reference: str = None) -> WalletTransaction:
    """
    Tambah saldo wallet user
    """
    if amount <= 0:
        raise ValidationError("Credit amount must be positive.")

    wallet.balance += amount
    wallet.save(update_fields=["balance", "updated_at"])

    return WalletTransaction.objects.create(
        tenant=tenant,
        wallet=wallet,
        amount=amount,
        transaction_type=transaction_type,
        description=description,
        reference=reference
    )


@transaction.atomic
def debit_wallet(*, tenant: Tenant, wallet: Wallet, amount: float, transaction_type: str,
                 description: str = "", reference: str = None) -> WalletTransaction:
    """
    Kurangi saldo wallet user
    """
    if amount <= 0:
        raise ValidationError("Debit amount must be positive.")
    if wallet.balance < amount:
        raise ValidationError("Insufficient balance.")

    wallet.balance -= amount
    wallet.save(update_fields=["balance", "updated_at"])

    return WalletTransaction.objects.create(
        tenant=tenant,
        wallet=wallet,
        amount=-amount,
        transaction_type=transaction_type,
        description=description,
        reference=reference
    )


# @transaction.atomic
# def pay_booking_from_wallet(*, tenant: Tenant, user: User, booking_id: int) -> dict:
#     from business.bookings.services.payment import pay_booking_with_wallet

#     # Ambil wallet & booking
#     wallet = Wallet.objects.filter(tenant=tenant, user=user, is_deleted=False).first()

#     if not wallet:
#         raise ValidationError("Wallet not found.")

#     booking = Booking.objects.filter(tenant=tenant, id=booking_id, is_deleted=False).first()

#     if not booking:
#         raise ValidationError("Booking not found.")

#     total_amount = Decimal(booking.total_price or 0)

#     if wallet.balance < total_amount:
#         raise ValidationError("Insufficient wallet balance.")

#     # Debit wallet
#     debit_wallet(
#         tenant=tenant,
#         wallet=wallet,
#         amount=float(total_amount),
#         transaction_type="payment",
#         reference=f"Booking {booking.booking_number}",
#         description=f"Payment for booking #{booking.id}"
#     )

#     # Confirm booking via business service
#     pay_booking_with_wallet(tenant=tenant, user=user, booking=booking)

#     return {
#         "wallet_balance": wallet.balance,
#         "booking_status": booking.status
#     }