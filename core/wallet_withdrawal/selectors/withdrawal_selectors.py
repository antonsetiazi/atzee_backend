# core/wallet_withdrawal/selectors/withdrawal_selectors.py

from core.wallet_withdrawal.models.withdrawal import Withdrawal


def get_user_withdrawals(*, tenant, user):
    return Withdrawal.objects.filter(
        tenant=tenant,
        user=user
    ).order_by("-created_at")


def get_withdrawal_by_id(*, tenant, user, withdrawal_id):
    return Withdrawal.objects.filter(
        tenant=tenant,
        user=user,
        id=withdrawal_id
    ).first()