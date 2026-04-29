# core/tenants/entities/tenant_branding.py

from core.entities.contracts import BaseEntity
from core.enum.permissions import CorePermission

class TenantBrandingEntity(BaseEntity):
    key = "tenant.branding"
    domain = "core"
    permission = CorePermission.ADMIN_TENANT_BRANDING_VIEW

    def query(self, *, user, tenant, query: dict) -> dict:
        branding = tenant.branding or {}

        theme = branding.get("theme", {})
        font = theme.get("font", {})

        return {
            "appName": branding.get("appName", ""),
            "logoUrl": branding.get("logoUrl", ""),
            "faviconUrl": branding.get("faviconUrl", ""),

            "theme": {
                "mode": theme.get("mode", "light"),

                "primary": theme.get("primary", ""),
                "secondary": theme.get("secondary", ""),
                "accent": theme.get("accent", ""),

                "background": theme.get("background", ""),
                "surface": theme.get("surface", ""),

                "textPrimary": theme.get("textPrimary", ""),
                "textSecondary": theme.get("textSecondary", ""),

                "radius": theme.get("radius", ""),
                "shadow": theme.get("shadow", ""),

                "font": {
                    "family": font.get("family", ""),
                    "size": font.get("size", ""),
                }
            }
        }