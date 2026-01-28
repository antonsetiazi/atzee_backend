from typing import Optional
from django.db.models import QuerySet

from accounting.chart_of_accounts.models import ChartOfAccount
from core.tenants.models import Tenant


def get_account_queryset(*, tenant: Tenant) -> QuerySet[ChartOfAccount]:
    """
    Base queryset for chart of accounts (tenant scoped).
    """
    return ChartOfAccount.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True
    )


def get_accounts(*, tenant: Tenant) -> QuerySet[ChartOfAccount]:
    """
    Get all accounts for a tenant.
    """
    return get_account_queryset(tenant=tenant).order_by("code")


def get_account_by_id(
    *,
    tenant: Tenant,
    account_id: int
) -> Optional[ChartOfAccount]:
    """
    Get single account by ID
    """
    try:
        return get_account_queryset(tenant=tenant).get(id=account_id)
    except ChartOfAccount.DoesNotExist:
        return None
    

def get_account_by_code(
    *,
    tenant: Tenant,
    code: str
) -> Optional[ChartOfAccount]:
    """
    Get single account by code (tenant-scoped).
    """
    try:
        return ChartOfAccount.objects.get(
            tenant=tenant,
            code=code,
            is_deleted=False
        )
    except ChartOfAccount.DoesNotExist:
        return None
    

def account_code_exists(
    *,
    tenant: Tenant,
    code: str,
    exclude_account_id: Optional[int] = None
) -> bool:
    qs = get_account_queryset(tenant=tenant).filter(code=code)

    if exclude_account_id:
        qs = qs.exclude(id=exclude_account_id)

    return qs.exists()