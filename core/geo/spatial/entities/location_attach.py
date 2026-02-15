# core/geo/spatial/entities/location_attach.py

from core.entities.contracts import BaseEntity
from core.geo.spatial.models import GeoLocation


class LocationAttachEntity(BaseEntity):
    key = "spatial.location.attach"
    domain = "core"
    permission = "core.geo.spatial.update"

    # WAJIB implement karena BaseEntity abstract
    def query(self, *, user, tenant, query: dict) -> dict:
        return {"items": [], "total": 0}

    def execute(self, *, user, tenant, data: dict) -> dict:
        """
        Attach new coordinate to an entity.
        """

        related_entity = data.get("related_entity")
        related_id = data.get("related_id")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        label = data.get("label")
        metadata = data.get("metadata", {})

        if not related_entity or not related_id:
            return {"success": False}

        if latitude is None or longitude is None:
            return {"success": False}

        location = GeoLocation.objects.create(
            tenant=tenant,
            related_entity=related_entity,
            related_id=str(related_id),
            latitude=latitude,
            longitude=longitude,
            label=label,
            metadata=metadata or {},
            created_by=user,
        )

        return {
            "success": True,
            "id": str(location.id),
        }
