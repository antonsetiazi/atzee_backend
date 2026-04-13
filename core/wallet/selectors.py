# core/wallet/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.wallet.models import Wallet, WalletTransaction
from core.tenants.models import Tenant
from core.users.models import User


def get_wallet(*, tenant: Tenant, user: User) -> Optional[Wallet]:
    return Wallet.objects.filter(
        tenant=tenant,
        user=user,
        is_deleted=False
    ).first()


def get_wallet_or_create(*, tenant: Tenant, user: User) -> Wallet:
    wallet, _ = Wallet.objects.get_or_create(
        tenant=tenant,
        user=user,
        defaults={
            "available_balance": 0,
            "held_balance": 0,
        }
    )
    return wallet


def get_wallet_transactions(
    *, tenant: Tenant, wallet: Wallet, limit: int = 50
) -> QuerySet[WalletTransaction]:
    return WalletTransaction.objects.filter(
        tenant=tenant,
        wallet=wallet,
        is_deleted=False
    ).order_by("-created_at")[:limit]


def get_system_wallet(*, tenant):
    """
    Get or create SYSTEM wallet (escrow pool)
    """
    system_user, _ = User.objects.get_or_create(
        username=f"system@{tenant.id}",
        defaults={
            "is_active": False,
        }
    )

    wallet, _ = Wallet.objects.get_or_create(
        tenant=tenant,
        user=system_user
    )

    return wallet