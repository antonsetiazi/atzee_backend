# core/classifications/tags/entities/tag_attached_list.py

from django.contrib.contenttypes.models import ContentType

from core.entities.contracts import BaseEntity
from core.classifications.tags.models import TagRelation


class TagAttachedListEntity(BaseEntity):
    key = "tags.attached.list"
    domain = "core"
    permission = "core.classifications.tags.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        model = query.get("model")
        object_id = query.get("object_id")

        if not model or not object_id:
            return {"items": [], "total": 0}

        app_label, model_name = model.split(".")

        try:
            content_type = ContentType.objects.get(
                app_label=app_label,
                model=model_name,
            )
        except ContentType.DoesNotExist:
            return {"items": [], "total": 0}

        qs = (
            TagRelation.objects
            .select_related("tag")
            .filter(
                tenant=tenant,
                content_type=content_type,
                object_id=object_id,
            )
        )

        data = [
            {
                "id": str(rel.tag.id),
                "code": rel.tag.code,
                "name": rel.tag.name,
                "description": rel.tag.description,
            }
            for rel in qs
        ]

        return {
            "items": data,
            "total": qs.count(),
        }
