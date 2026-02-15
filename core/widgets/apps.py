# core/widgets/apps.py

from django.apps import AppConfig


class WidgetsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.widgets"
    label = "core_widgets"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.widget_list import WidgetListEntity
        from .entities.widget_select_list import WidgetSelectListEntity
        from .entities.widget_banner_dashboard import WidgetBannerDashboardEntity

        register_entity(WidgetListEntity())
        register_entity(WidgetSelectListEntity())
        register_entity(WidgetBannerDashboardEntity())

