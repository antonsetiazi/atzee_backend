# core/widgets/entities/widget_banner_dashboard.py

from django.utils import timezone
from django.db import models
from core.entities.contracts import BaseEntity
from core.widgets.models import UIWidget


class WidgetBannerDashboardEntity(BaseEntity):
    key = "widgets.banner.dashboard"
    domain = "core"
    permission = "core.dashboard.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        now = timezone.now()

        qs = UIWidget.objects.filter(
            tenant=tenant,
            type="banner",
            is_deleted=False,
            is_active=True,
        ).filter(
            models.Q(starts_at__isnull=True) | models.Q(starts_at__lte=now)
        ).filter(
            models.Q(ends_at__isnull=True) | models.Q(ends_at__gte=now)
        ).order_by("order")

        items = []

        for w in qs:
            config = w.config or {}
            
            if isinstance(config, list):
                config = config[0] if config else {}

            items.append({
                "id": str(w.id),
                "title": w.title,
                "image_url": config.get("image_url"),
                "link_url": config.get("link_url"),
                "open_in_new_tab": config.get("open_in_new_tab", True),
            })

        return {
            "items": items,
            "total": qs.count(),
        }
