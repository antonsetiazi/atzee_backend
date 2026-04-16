# core/wallet/services.py

from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError

from core.wallet.models import Wallet, WalletTransaction, WalletTransactionType


# ==============================
# INTERNAL HELPER
# ==============================

def _get_locked_wallet(wallet_id: int) -> Wallet:
    return Wallet.objects.select_for_update().get(id=wallet_id)


def _check_idempotency(idempotency_key: str) -> bool:
    return WalletTransaction.objects.filter(idempotency_key=idempotency_key).exists()


def _create_transaction(
    *, tenant, wallet, amount: Decimal,
    tx_type: str,
    reference_type: str = None,
    reference_id: str = None,
    idempotency_key: str,
    description: str = "",
    meta: dict | None = None,
):
    return WalletTransaction.objects.create(
        tenant=tenant,
        wallet=wallet,
        amount=amount,
        transaction_type=tx_type,
        reference_type=reference_type,
        reference_id=reference_id,
        idempotency_key=idempotency_key,
        description=description,
        meta=meta or {},
    )


# ==============================
# BASIC OPERATIONS
# ==============================

@transaction.atomic
def topup_wallet(
    *, tenant, wallet: Wallet, amount: Decimal,
    idempotency_key: str,
    description: str = "",
):
    """
    Topup wallet (manual / payment gateway success)
    """
    if amount <= 0:
        raise ValidationError("Amount must be positive.")

    if _check_idempotency(idempotency_key):
        return

    wallet = _get_locked_wallet(wallet.id)

    wallet.available_balance += amount
    wallet.save(update_fields=["available_balance", "updated_at"])

    return _create_transaction(
        tenant=tenant,
        wallet=wallet,
        amount=amount,
        tx_type=WalletTransactionType.TOPUP,
        idempotency_key=idempotency_key,
        description=description,
        meta={
            "flow": "topup",
            "source": "midtrans",
            "channel": "unknown",  # nanti bisa diisi dari payment gateway
            "actor": "system",
        }
    )


@transaction.atomic
def debit_wallet(
    *, tenant, wallet: Wallet, amount: Decimal,
    idempotency_key: str,
    description: str = "",
):
    """
    Direct debit (non-escrow use only)
    """
    if amount <= 0:
        raise ValidationError("Amount must be positive.")

    if _check_idempotency(idempotency_key):
        return

    wallet = _get_locked_wallet(wallet.id)

    if wallet.available_balance < amount:
        raise ValidationError("Insufficient balance.")

    wallet.available_balance -= amount
    wallet.save(update_fields=["available_balance", "updated_at"])

    return _create_transaction(
        tenant=tenant,
        wallet=wallet,
        amount=-amount,
        tx_type=WalletTransactionType.PAYMENT,
        idempotency_key=idempotency_key,
        description=description,
    )


# ==============================
# ESCROW ENGINE
# ==============================

@transaction.atomic
def escrow_hold(
    *, tenant, wallet: Wallet, amount: Decimal,
    reference_type: str,
    reference_id: str,
    idempotency_key: str,
    description: str = "",
):
    """
    Move money from available → held (user pays, money held)
    """
    if amount <= 0:
        raise ValidationError("Amount must be positive.")

    if _check_idempotency(idempotency_key):
        return

    wallet = _get_locked_wallet(wallet.id)

    if wallet.available_balance < amount:
        raise ValidationError("Insufficient balance.")

    wallet.available_balance -= amount
    wallet.held_balance += amount
    wallet.save(update_fields=["available_balance", "held_balance", "updated_at"])

    return _create_transaction(
        tenant=tenant,
        wallet=wallet,
        amount=-amount,
        tx_type=WalletTransactionType.ESCROW_HOLD,
        reference_type=reference_type,
        reference_id=reference_id,
        idempotency_key=idempotency_key,
        description=description,
        meta={
            "flow": "escrow",
            "actor": "user",
            "order_id": reference_id,
        }
    )


@transaction.atomic
def escrow_release_to_partner(
    *, tenant,
    user_wallet: Wallet,
    partner_wallet: Wallet,
    amount: Decimal,
    reference_type: str,
    reference_id: str,
    idempotency_key: str,
    description: str = "",
):
    """
    Release escrow → move from user held → partner available
    """
    if amount <= 0:
        raise ValidationError("Amount must be positive.")

    if _check_idempotency(idempotency_key):
        return

    # 🔒 Lock BOTH wallets (IMPORTANT)
    user_wallet = Wallet.objects.select_for_update().get(id=user_wallet.id)
    partner_wallet = Wallet.objects.select_for_update().get(id=partner_wallet.id)

    if user_wallet.held_balance < amount:
        raise ValidationError("Invalid held balance.")

    # user: held ↓
    user_wallet.held_balance -= amount
    user_wallet.save(update_fields=["held_balance", "updated_at"])

    # partner: available ↑
    partner_wallet.available_balance += amount
    partner_wallet.save(update_fields=["available_balance", "updated_at"])

    # ledger: user side (release out)
    _create_transaction(
        tenant=tenant,
        wallet=user_wallet,
        amount=-amount,
        tx_type=WalletTransactionType.ESCROW_RELEASE,
        reference_type=reference_type,
        reference_id=reference_id,
        idempotency_key=f"{idempotency_key}-user",
        description="Escrow released to partner",
        meta={
            "flow": "payout",
            "actor": "system",
            "order_id": reference_id,
        }
    )

    # ledger: partner side (receive)
    return _create_transaction(
        tenant=tenant,
        wallet=partner_wallet,
        amount=amount,
        tx_type=WalletTransactionType.ESCROW_RELEASE,
        reference_type=reference_type,
        reference_id=reference_id,
        idempotency_key=f"{idempotency_key}-partner",
        description=description or "Receive from escrow",
        meta={
            "flow": "payout",
            "actor": "partner",
            "order_id": reference_id,
        }
    )


@transaction.atomic
def escrow_refund(
    *, tenant,
    wallet: Wallet,
    amount: Decimal,
    reference_type: str,
    reference_id: str,
    idempotency_key: str,
    description: str = "",
):
    """
    Refund escrow → move from held → available (back to user)
    """
    if amount <= 0:
        raise ValidationError("Amount must be positive.")

    if _check_idempotency(idempotency_key):
        return

    wallet = _get_locked_wallet(wallet.id)

    if wallet.held_balance < amount:
        raise ValidationError("Invalid held balance.")

    wallet.held_balance -= amount
    wallet.available_balance += amount
    wallet.save(update_fields=["held_balance", "available_balance", "updated_at"])

    return _create_transaction(
        tenant=tenant,
        wallet=wallet,
        amount=amount,
        tx_type=WalletTransactionType.REFUND,
        reference_type=reference_type,
        reference_id=reference_id,
        idempotency_key=idempotency_key,
        description=description or "Refund from escrow",
        meta={
            "flow": "refund",
            "actor": "system",
            "order_id": reference_id,
        }
    )