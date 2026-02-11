# core/files/entities/file_select_list.py

from core.entities.contracts import BaseEntity
from core.files.models import File


class FileSelectListEntity(BaseEntity):
    """
    files.select.list entity

    Used for dropdown or lightweight selection.
    """

    key = "files.select.list"
    domain = "core"
    permission = "core.files.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        related_entity = query.get("related_entity")
        related_id = query.get("related_id")

        qs = File.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        if related_entity:
            qs = qs.filter(related_entity=related_entity)

        if related_id:
            qs = qs.filter(related_id=related_id)

        qs = qs.order_by("-created_at")

        items = [
            {
                "value": str(f.id),
                "label": f.original_name,
            }
            for f in qs
        ]

        return {
            "items": items,
            "total": qs.count(),
        }
