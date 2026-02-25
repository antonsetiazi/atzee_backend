# core/wallet/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.wallet.models import Wallet, WalletTransaction
from core.tenants.models import Tenant
from core.users.models import User


def get_wallet(*, tenant: Tenant, user: User) -> Optional[Wallet]:
    try:
        return Wallet.objects.get(tenant=tenant, user=user, is_deleted=False)
    except Wallet.DoesNotExist:
        return None


def get_wallet_transactions(*, wallet: Wallet) -> QuerySet[WalletTransaction]:
    return wallet.transactions.filter(is_deleted=False).order_by("-created_at")