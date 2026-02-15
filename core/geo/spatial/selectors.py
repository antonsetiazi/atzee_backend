# core/geo/spatial/selectors.py

from typing import Optional
from django.db.models import QuerySet

from core.geo.spatial.models import GeoLocation
from core.tenants.models import Tenant


def get_location_queryset(*, tenant: Tenant) -> QuerySet[GeoLocation]:
    """
    Base queryset for GeoLocation (tenant scoped).
    """
    return GeoLocation.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_locations_by_relation(
    *,
    tenant: Tenant,
    related_entity: str,
    related_id
) -> QuerySet[GeoLocation]:
    """
    Get all spatial locations attached to an entity.
    """
    return get_location_queryset(
        tenant=tenant
    ).filter(
        related_entity=related_entity,
        related_id=related_id
    )


def get_location_by_id(
    *,
    tenant: Tenant,
    location_id: int
) -> Optional[GeoLocation]:
    try:
        return get_location_queryset(
            tenant=tenant
        ).get(id=location_id)
    except GeoLocation.DoesNotExist:
        return None
