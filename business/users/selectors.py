# business/users/selectors.py

from typing import Optional
from django.db.models import QuerySet, Q

from business.users.models import BusinessUser
from core.tenants.models import Tenant


def get_user_queryset(*, tenant: Tenant) -> QuerySet[BusinessUser]:
    return BusinessUser.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_users(*, tenant: Tenant) -> QuerySet[BusinessUser]:
    return get_user_queryset(tenant=tenant).order_by("name")


def get_user_by_id(*, tenant: Tenant, user_id: int) -> Optional[BusinessUser]:
    try:
        return get_user_queryset(tenant=tenant).get(id=user_id)
    except BusinessUser.DoesNotExist:
        return None


def get_user_by_core_user(*, tenant: Tenant, core_user_id: int) -> Optional[BusinessUser]:
    try:
        return get_user_queryset(tenant=tenant).get(core_user_id=core_user_id)
    except BusinessUser.DoesNotExist:
        return None


def search_users(*, tenant: Tenant, keyword: str) -> QuerySet[BusinessUser]:
    return (
        get_user_queryset(tenant=tenant)
        .filter(
            Q(name__icontains=keyword)
            | Q(phone__icontains=keyword)
            | Q(organization_name__icontains=keyword)
        )
        .order_by("name")
    )
