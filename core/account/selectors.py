# core/account/selectors.py

from core.account.models import UserAddress


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