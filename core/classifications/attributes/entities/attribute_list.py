# core/classifications/attributes/entities/attribute_list.py

from core.entities.contracts import BaseEntity
from core.classifications.attributes.models.attribute import Attribute


class AttributeListEntity(BaseEntity):
    """
    attributes.list entity
    """

    key = "attributes.list"
    domain = "core"
    permission = "core.attributes.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = Attribute.objects.filter(
            tenant=tenant,
            is_deleted=False,
            is_active=True,
        )

        # optional filters
        scope = query.get("scope")
        if scope:
            qs = qs.filter(scope=scope)

        attr_type = query.get("type")
        if attr_type:
            qs = qs.filter(type=attr_type)

        search = query.get("search")
        if search:
            qs = qs.filter(name__icontains=search)

        qs = qs.order_by("scope", "name")

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs[offset:limit]

        data = [
            {
                "id": str(a.id),
                "scope": a.scope,
                "code": a.code,
                "name": a.name,
                "type": a.type,
            }
            for a in items
        ]

        return {
            "items": data,
            "total": total,
        }
