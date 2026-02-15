# core/geo/spatial/entities/location_list.py

from core.entities.contracts import BaseEntity
from core.geo.spatial.models import GeoLocation


class LocationListEntity(BaseEntity):
    key = "spatial.location.list"
    domain = "core"
    permission = "core.geo.spatial.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        related_entity = query.get("related_entity")
        related_id = query.get("related_id")

        if not related_entity or not related_id:
            return {"items": [], "total": 0}

        qs = GeoLocation.objects.filter(
            tenant=tenant,
            is_deleted=False,
            related_entity=related_entity,
            related_id=str(related_id),
        ).order_by("-created_at")

        data = [
            {
                "id": str(loc.id),
                "latitude": loc.latitude,
                "longitude": loc.longitude,
                "label": loc.label,
                "metadata": loc.metadata,
                "created_at": loc.created_at,
            }
            for loc in qs
        ]

        return {
            "items": data,
            "total": qs.count(),
        }
