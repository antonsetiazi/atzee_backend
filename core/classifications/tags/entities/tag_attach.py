# core/classifications/tags/entities/tag_attach.py

from django.contrib.contenttypes.models import ContentType

from core.entities.contracts import BaseEntity
from core.classifications.tags.models import TagRelation, Tag


class TagAttachEntity(BaseEntity):
    key = "tags.attach"
    domain = "core"
    permission = "core.tags.update"

    # ✅ WAJIB ADA karena BaseEntity abstract
    def query(self, *, user, tenant, query: dict) -> dict:
        return {"items": [], "total": 0}

    def execute(self, *, user, tenant, data: dict) -> dict:

        tag_id = data.get("tag_id")
        model = data.get("model")       # contoh: "customers.customer"
        object_id = data.get("object_id")

        if not tag_id or not model or not object_id:
            return {"success": False}

        app_label, model_name = model.split(".")

        content_type = ContentType.objects.get(
            app_label=app_label,
            model=model_name,
        )

        tag = Tag.objects.filter(
            id=tag_id,
            tenant=tenant,
        ).first()

        if not tag:
            return {"success": False}

        TagRelation.objects.get_or_create(
            tenant=tenant,
            tag=tag,
            content_type=content_type,
            object_id=object_id,
        )

        return {"success": True}
