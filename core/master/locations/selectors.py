# core/master/locations/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.master.locations.models import Location
from core.tenants.models import Tenant


def get_location_queryset(*, tenant: Tenant) -> QuerySet[Location]:
    return Location.objects.filter(
        tenant=tenant,
        is_deleted=False,
        is_active=True
    )


def get_locations(*, tenant: Tenant) -> QuerySet[Location]:
    return get_location_queryset(
        tenant=tenant
    ).select_related("parent").order_by("name")


def get_location_by_id(
    *, tenant: Tenant, location_id: int
) -> Optional[Location]:
    try:
        return get_location_queryset(
            tenant=tenant
        ).get(id=location_id)
    except Location.DoesNotExist:
        return None
