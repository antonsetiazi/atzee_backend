# core/account/selectors.py

from core.account.models import UserAddress
from core.account.models import UserBankAccount


def get_user_addresses(*, tenant, user):
    return UserAddress.objects.filter(
        tenant=tenant,
        user=user,
        is_active=True,
    ).order_by("-is_default", "-created_at")


def get_user_address_by_id(*, tenant, user, address_id):
    return UserAddress.objects.filter(
        tenant=tenant,
        user=user,
        id=address_id,
        is_active=True,
    ).first()


def get_user_banks(*, tenant, user):
    return UserBankAccount.objects.filter(
        tenant=tenant,
        user=user,
        is_active=True,
    ).order_by("-is_default", "-created_at")


def get_user_bank_by_id(*, tenant, user, bank_id):
    return UserBankAccount.objects.filter(
        tenant=tenant,
        user=user,
        id=bank_id,
        is_active=True,
    ).first()