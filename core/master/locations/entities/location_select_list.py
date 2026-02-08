# core/master/locations/entities/location_select_list.py

from core.entities.contracts import BaseEntity
from core.master.locations.models import Location


class LocationSelectListEntity(BaseEntity):
    """
    locations.select.list entity
    Used for select field (parent location, etc)
    """

    key = "locations.select.list"
    domain = "core"
    permission = "core.location.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Location.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        ).select_related("parent").order_by("name")

        items = [
            {
                "value": str(loc.id),
                "label": (
                    f"{loc.parent.name} / {loc.name}"
                    if loc.parent else loc.name
                ),
            }
            for loc in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
