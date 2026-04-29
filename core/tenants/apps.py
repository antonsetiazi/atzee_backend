from django.apps import AppConfig


class TenantsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.tenants"
    label = "core_tenants"


    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.tenant_branding import TenantBrandingEntity
        from .entities.tenant_branding_update import TenantBrandingUpdateEntity

        register_entity(TenantBrandingEntity())
        register_entity(TenantBrandingUpdateEntity())