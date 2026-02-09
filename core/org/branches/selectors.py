# core/org/branches/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.org.branches.models import Branch
from core.tenants.models import Tenant


def get_branch_queryset(*, tenant: Tenant) -> QuerySet[Branch]:
    return Branch.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True
    )


def get_branches(*, tenant: Tenant) -> QuerySet[Branch]:
    return get_branch_queryset(tenant=tenant).order_by("name")


def get_branch_by_id(
    *, tenant: Tenant, branch_id: int
) -> Optional[Branch]:
    try:
        return get_branch_queryset(
            tenant=tenant
        ).get(id=branch_id)
    except Branch.DoesNotExist:
        return None
