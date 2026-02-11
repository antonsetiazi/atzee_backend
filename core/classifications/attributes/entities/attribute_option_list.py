# core/classifications/attributes/entities/attribute_option_list.py

from core.entities.contracts import BaseEntity
from core.classifications.attributes.models import AttributeOption


class AttributeOptionListEntity(BaseEntity):
    """
    attribute.options.list entity

    Used for:
    - dropdown options
    - nested option list under attribute
    """

    key = "attribute.options.list"
    domain = "core"
    permission = "core.attributes.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        """
        Supported query params:
        - attribute_id (required / optional tergantung UI)
        - is_active (optional)
        """

        qs = AttributeOption.objects.filter(
            tenant=tenant,
        )

        attribute_id = query.get("attribute_id")
        if attribute_id:
            qs = qs.filter(attribute_id=attribute_id)

        is_active = query.get("is_active")
        if is_active is not None:
            qs = qs.filter(is_active=is_active)

        qs = qs.select_related("attribute").order_by("name")

        return {
            "total": qs.count(),
            "items": [
                {
                    "id": obj.id,
                    "code": obj.code,
                    "name": obj.name,
                    "attribute": {
                        "id": obj.attribute_id,
                        "code": obj.attribute.code,
                        "name": obj.attribute.name,
                    },
                    "is_active": obj.is_active,
                }
                for obj in qs
            ],
        }
