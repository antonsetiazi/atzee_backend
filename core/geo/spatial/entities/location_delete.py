# core/geo/spatial/entities/location_delete.py

from core.entities.contracts import BaseEntity
from core.geo.spatial.models import GeoLocation


class LocationDeleteEntity(BaseEntity):
    key = "spatial.location.delete"
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

        location.is_deleted = True
        location.updated_by = user
        location.save(update_fields=[
            "is_deleted",
            "updated_by",
            "updated_at",
        ])

        return {"success": True}
