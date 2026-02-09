# core/geo/countries/selectors.py

from typing import Optional
from django.db.models import QuerySet
from core.geo.countries.models import Country
from core.tenants.models import Tenant


def get_country_queryset(*, tenant: Tenant) -> QuerySet[Country]:
    return Country.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True,
    )


def get_countries(*, tenant: Tenant) -> QuerySet[Country]:
    return get_country_queryset(tenant=tenant)


def get_country_by_id(
    *, tenant: Tenant, country_id: int
) -> Optional[Country]:
    try:
        return get_country_queryset(
            tenant=tenant
        ).get(id=country_id)
    except Country.DoesNotExist:
        return None
