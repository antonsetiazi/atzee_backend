# verticals/ustadzku/apps.py

from django.apps import AppConfig

class UstadzkuConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verticals.ustadzku"
    label = "verticals_ustadzku"

    def ready(self):
        from .ui import bootstrap  
        import verticals.ustadzku.seeds.permissions

        from core.entities.registry import register_entity
        from verticals.ustadzku.entities.guest_home import GuestHomeEntity
        from verticals.ustadzku.entities.admin_dashboard import AdminDashboardEntity
        from verticals.ustadzku.entities.user_dashboard import UserDashboardEntity
        from verticals.ustadzku.entities.partner_dashboard import PartnerDashboardEntity

        register_entity(GuestHomeEntity())
        register_entity(AdminDashboardEntity())
        register_entity(UserDashboardEntity())
        register_entity(PartnerDashboardEntity())