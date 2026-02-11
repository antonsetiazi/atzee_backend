# core/classifications/attributes/entities/attribute_select_list.py

from core.entities.contracts import BaseEntity
from core.classifications.attributes.models.attribute import Attribute


class AttributeSelectListEntity(BaseEntity):
    """
    attributes.select.list entity
    """

    key = "attributes.select.list"
    domain = "core"
    permission = "core.attributes.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Attribute.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        )

        scope = query.get("scope")
        if scope:
            qs = qs.filter(scope=scope)

        qs = qs.order_by("name")

        items = [
            {
                "value": str(a.id),
                "label": a.name,
                "type": a.type,
            }
            for a in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
