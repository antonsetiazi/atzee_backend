# business/partners/selectors.py

from typing import Optional
from django.db.models import QuerySet, Q

from business.partners.models import Partner
from core.tenants.models import Tenant


def get_partner_queryset(*, tenant: Tenant) -> QuerySet[Partner]:
    """
    Base queryset for partner (tenant scoped).
    """
    return Partner.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_partners(*, tenant: Tenant) -> QuerySet[Partner]:
    """
    Get all partners for a tenant.
    """
    return (
        get_partner_queryset(tenant=tenant)
        .order_by("name")
    )


def get_partner_by_id(*, tenant: Tenant, partner_id: int) -> Optional[Partner]:
    """
    Get single partner by ID.
    """
    try:
        return get_partner_queryset(tenant=tenant).get(id=partner_id)
    except Partner.DoesNotExist:
        return None
    

def search_partners(*, tenant: Tenant, keyword: str) -> QuerySet[Partner]: 
    """
    Search partner by name, phone, or email.
    """
    return (
        get_partner_queryset(tenant=tenant)
        .filter(
            Q(name__icontains=keyword)
            | Q(phone__icontains=keyword)
            | Q(email__icontains=keyword)
        )
        .order_by("name")
    )


def partner_exists(*, tenant: Tenant, partner_id: int) -> bool:
    return get_partner_queryset(tenant=tenant).filter(
        id=partner_id
    ).exists()


def get_marketplace_partner_queryset(*, tenant: Tenant) -> QuerySet[Partner]:
    return (
        get_partner_queryset(tenant=tenant)
        .filter(search_latitude__isnull=False)
    )


def get_my_partner(*, tenant, user):
    return Partner.objects.filter(
        tenant=tenant,
        core_user=user,
        is_deleted=False,
    ).first()