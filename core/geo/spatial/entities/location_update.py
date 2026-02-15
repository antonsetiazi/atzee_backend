# core/geo/spatial/entities/location_update.py

from core.entities.contracts import BaseEntity
from core.geo.spatial.models import GeoLocation


class LocationUpdateEntity(BaseEntity):
    key = "spatial.location.update"
    domain = "core"
    permission = "core.geo.spatial.update"

    def query(self, *, user, tenant, query: dict) -> dict:
        return {"items": [], "total": 0}

    def execute(self, *, user, tenant, data: dict) -> dict:
        location_id = data.get("id")

        if not location_id:
            return {"success": False}

        location = GeoLocation.objects.filter(
            tenant=tenant,
            id=location_id,
            is_deleted=False,
        ).first()

        if not location:
            return {"success": False}

        if "latitude" in data:
            location.latitude = data["latitude"]

        if "longitude" in data:
            location.longitude = data["longitude"]

        if "label" in data:
            location.label = data["label"]

        if "metadata" in data:
            location.metadata = data["metadata"]

        location.updated_by = user
        location.save(update_fields=[
            "latitude",
            "longitude",
            "label",
            "metadata",
            "updated_by",
            "updated_at",
        ])

        return {"success": True}
