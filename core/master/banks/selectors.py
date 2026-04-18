# core/master/banks/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.master.banks.models import Bank
from core.tenants.models import Tenant


def get_bank_queryset(*, tenant: Tenant) -> QuerySet[Bank]:
    return Bank.objects.filter(
        tenant=tenant,
        is_deleted=False,
    )


def get_banks(
    *,
    tenant: Tenant,
    active_only: bool = True,
) -> QuerySet[Bank]:

    qs = get_bank_queryset(tenant=tenant)

    if active_only:
        qs = qs.filter(is_active=True)

    return qs


def get_bank_by_id(
    *,
    tenant: Tenant,
    bank_id: int,
) -> Optional[Bank]:
    try:
        return get_bank_queryset(
            tenant=tenant
        ).get(id=bank_id)
    except Bank.DoesNotExist:
        return None