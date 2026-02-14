# core/widgets/entities/widget_list.py

from core.entities.contracts import BaseEntity
from django.utils import timezone
from django.db import models

from core.widgets.models import UIWidget


class WidgetListEntity(BaseEntity):
    """
    widgets.list entity
    """

    key = "widgets.list"
    domain = "core"
    permission = "core.widgets.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        qs = UIWidget.objects.filter(
            tenant=tenant,
            is_deleted=False,
        )

        # Optional filter by type
        widget_type = query.get("type")
        
        if widget_type:
            qs = qs.filter(type=widget_type)

        # Optional filter by position
        position = query.get("position")
        if position:
            qs = qs.filter(position=position)

        # Optional filter by active status
        is_active = query.get("is_active")
        if is_active is not None:
            qs = qs.filter(is_active=is_active in ["true", "1", True])

        # Optional filter by schedule (only currently active)
        now_only = query.get("now")
        if now_only in ["true", "1", True]:
            now = timezone.now()
            qs = qs.filter(
                is_active=True
            ).filter(
                models.Q(starts_at__isnull=True) | models.Q(starts_at__lte=now)
            ).filter(
                models.Q(ends_at__isnull=True) | models.Q(ends_at__gte=now)
            )

        # Search by title
        search = query.get("search")
        if search:
            qs = qs.filter(title__icontains=search)

        page = int(query.get("page", 1))
        page_size = int(query.get("pageSize", 10))

        offset = (page - 1) * page_size
        limit = offset + page_size

        total = qs.count()
        items = qs.order_by("order", "-created_at")[offset:limit]

        data = [
            {
                "id": str(w.id),
                "type": w.type,
                "position": w.position,
                "title": w.title,
                "order": w.order,
                "is_active": w.is_active,
                "starts_at": w.starts_at,
                "ends_at": w.ends_at,
                "created_at": w.created_at,
            }
            for w in items
        ]

        return {
            "items": data,
            "total": total,
        }
