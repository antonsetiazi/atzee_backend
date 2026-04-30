# core/widgets/entities/widget_banner_dashboard.py

from core.entities.contracts import BaseEntity
from core.widgets.selectors import get_active_widgets_for_user

class WidgetBannerDashboardEntity(BaseEntity):
    key = "widgets.banner.dashboard"
    domain = "core"
    permission = "core.dashboard.view"

    def query(self, *, user, tenant, query: dict) -> dict:
        widgets = get_active_widgets_for_user(
            tenant=tenant,
            user=user,
            position="dashboard.main",
        )

        items = []

        for w in widgets:
            if w.type != "banner":
                continue

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
            "total": len(items),
        }
