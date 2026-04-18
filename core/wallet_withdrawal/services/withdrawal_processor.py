# core/wallet_withdrawal/services/withdrawal_processor.py

from django.db import transaction
from django.utils import timezone

from core.wallet_withdrawal.models.withdrawal import Withdrawal, WithdrawalStatus


@transaction.atomic
def mark_as_processing(withdrawal: Withdrawal):
    if withdrawal.status != WithdrawalStatus.PENDING:
        return

    withdrawal.status = WithdrawalStatus.PROCESSING
    withdrawal.save(update_fields=["status"])


@transaction.atomic
def mark_as_completed(withdrawal: Withdrawal, external_id: str = ""):
    if withdrawal.status not in [WithdrawalStatus.PENDING, WithdrawalStatus.PROCESSING]:
        return

    withdrawal.status = WithdrawalStatus.COMPLETED
    withdrawal.external_id = external_id
    withdrawal.processed_at = timezone.now()
    withdrawal.save(update_fields=["status", "external_id", "processed_at"])


@transaction.atomic
def mark_as_failed(withdrawal: Withdrawal, reason: str = ""):
    """
    BALIKKAN SALDO jika gagal
    """

    if withdrawal.status not in [WithdrawalStatus.PENDING, WithdrawalStatus.PROCESSING]:
        return

    wallet = withdrawal.wallet

    total_refund = withdrawal.amount + withdrawal.fee

    wallet.available_balance += total_refund
    wallet.save(update_fields=["available_balance"])

    withdrawal.status = WithdrawalStatus.FAILED
    withdrawal.failed_reason = reason
    withdrawal.save(update_fields=["status", "failed_reason"])