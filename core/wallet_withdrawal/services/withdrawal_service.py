# core/wallet_withdrawal/services/withdrawal_service.py

from decimal import Decimal
from django.db import transaction
from django.utils.crypto import get_random_string
from rest_framework.exceptions import ValidationError

from core.wallet import selectors as wallet_selectors
from core.wallet import services as wallet_services

from core.wallet_withdrawal.models.withdrawal import Withdrawal, WithdrawalStatus
from core.account.selectors import get_user_bank_by_id


MIN_WITHDRAW_AMOUNT = Decimal("50000")
WITHDRAW_FEE = Decimal("2500")


def generate_idempotency(prefix: str) -> str:
    return f"{prefix}_{get_random_string(20)}"


@transaction.atomic
def request_withdrawal(*, tenant, user, amount: Decimal, destination_bank_id) -> Withdrawal:
    """
    Create withdrawal request (SAFE & CONSISTENT WITH WALLET)
    """

    # ==============================
    # VALIDATION
    # ==============================
    if amount < MIN_WITHDRAW_AMOUNT:
        raise ValidationError("Minimum withdrawal is 50.000")

    if amount <= 0:
        raise ValidationError("Invalid amount")

    # 🔥 GET BANK
    user_bank  = get_user_bank_by_id(
        tenant=tenant,
        user=user,
        bank_id=destination_bank_id
    )

    if not user_bank:
        raise ValidationError("Bank account not found")
    
    # 🔥 SNAPSHOT
    destination = {
        "user_bank_id": user_bank.id,
        "bank_name": user_bank.bank.name,
        "bank_code": getattr(user_bank.bank, "code", ""),
        "account_number": user_bank.account_number,
        "account_name": user_bank.account_name,
    }

    # ==============================
    # GET WALLET (FIXED)
    # ==============================
    wallet = wallet_selectors.get_wallet_or_create(
        tenant=tenant,
        user=user
    )

    total_deduction = amount + WITHDRAW_FEE

    if wallet.available_balance < total_deduction:
        raise ValidationError("Insufficient balance")

    # ==============================
    # IDEMPOTENCY
    # ==============================
    idempotency_key = generate_idempotency("withdraw")

    # ==============================
    # DEBIT WALLET (🔥 FIX UTAMA)
    # ==============================
    wallet_services.debit_wallet(
        tenant=tenant,
        wallet=wallet,
        amount=total_deduction,
        idempotency_key=idempotency_key,
        description="Withdraw request",
    )
    
    # ==============================
    # CREATE WITHDRAWAL
    # ==============================
    withdrawal = Withdrawal.objects.create(
        tenant=tenant,  # 🔥 WAJIB
        user=user,
        wallet=wallet,
        amount=amount,
        fee=WITHDRAW_FEE,
        destination=destination,
        status=WithdrawalStatus.PENDING,
    )

    return withdrawal