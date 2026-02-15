# core/geo/spatial/services.py

from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.geo.spatial.models import GeoLocation
from core.geo.spatial import selectors
from core.tenants.models import Tenant
from core.users.models import User


def _validate_coordinate_range(latitude, longitude):
    if not (-90 <= latitude <= 90):
        raise ValidationError("Latitude must be between -90 and 90.")

    if not (-180 <= longitude <= 180):
        raise ValidationError("Longitude must be between -180 and 180.")


@transaction.atomic
def create_location(
    *,
    tenant: Tenant,
    created_by: User,
    related_entity: str,
    related_id,
    latitude,
    longitude,
    label: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> GeoLocation:
    """
    Create new spatial location.
    """

    if not related_entity:
        raise ValidationError("related_entity is required.")

    if not related_id:
        raise ValidationError("related_id is required.")

    _validate_coordinate_range(latitude, longitude)

    return GeoLocation.objects.create(
        tenant=tenant,
        related_entity=related_entity,
        related_id=related_id,
        latitude=latitude,
        longitude=longitude,
        label=label,
        metadata=metadata or {},
        created_by=created_by
    )


@transaction.atomic
def update_location(
    *,
    tenant: Tenant,
    location_id: int,
    updated_by: User,
    latitude=None,
    longitude=None,
    label: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> GeoLocation:

    location = selectors.get_location_by_id(
        tenant=tenant,
        location_id=location_id
    )

    if not location:
        raise ValidationError("Location not found.")

    if latitude is not None:
        if not (-90 <= latitude <= 90):
            raise ValidationError("Invalid latitude.")
        location.latitude = latitude

    if longitude is not None:
        if not (-180 <= longitude <= 180):
            raise ValidationError("Invalid longitude.")
        location.longitude = longitude

    if label is not None:
        location.label = label

    if metadata is not None:
        location.metadata = metadata

    location.updated_by = updated_by
    location.save(update_fields=[
        "latitude",
        "longitude",
        "label",
        "metadata",
        "updated_by",
        "updated_at"
    ])

    return location


@transaction.atomic
def delete_location(
    *,
    tenant: Tenant,
    location_id: int,
    deleted_by: User
) -> None:

    location = selectors.get_location_by_id(
        tenant=tenant,
        location_id=location_id
    )

    if not location:
        raise ValidationError("Location not found.")

    location.is_deleted = True
    location.updated_by = deleted_by
    location.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at"
    ])
