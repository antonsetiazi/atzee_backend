# core/tenants/entities/tenant_branding_update.py

from copy import deepcopy
from core.entities.contracts import BaseEntity
from core.enum.permissions import CorePermission

class TenantBrandingUpdateEntity(BaseEntity):
    key = "tenant.branding.update"
    domain = "core"
    permission = CorePermission.ADMIN_TENANT_BRANDING_UPDATE

    def query(self, *, user, tenant, query: dict) -> dict:
        return {}

    def execute(self, *, user, tenant, data: dict) -> dict:
        branding = deepcopy(tenant.branding or {})

        # ===============================
        # ROOT LEVEL
        # ===============================
        branding["appName"] = data.get(
            "appName",
            branding.get("appName")
        )

        branding["logoUrl"] = data.get(
            "logoUrl",
            branding.get("logoUrl")
        )

        branding["faviconUrl"] = data.get(
            "faviconUrl",
            branding.get("faviconUrl")
        )

        # ===============================
        # THEME
        # ===============================
        theme = branding.setdefault("theme", {})
        incoming_theme = data.get("theme", {})

        for key, value in incoming_theme.items():
            if key != "font":
                theme[key] = value

        # ===============================
        # FONT
        # ===============================
        font = theme.setdefault("font", {})
        incoming_font = incoming_theme.get("font", {})

        for key, value in incoming_font.items():
            font[key] = value

        # ===============================
        tenant.branding = branding
        tenant.save(update_fields=["branding"])

        return {
            "success": True,
            "message": "Branding updated successfully."
        }