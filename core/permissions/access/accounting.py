# core/permissions/access/accounting.py

from core.permissions.access.base import BaseAccessPolicy


class IsAccountingAdmin(BaseAccessPolicy):
    """
    Accounting admin access.
    """

    domain = "accounting"
    min_level = ("manager", "admin", "superadmin")


class IsAccountingPoster(IsAccountingAdmin):
    """
    Allows posting accounting journals.
    """

    action_permission = "accounting.journal.post"

    def has_permission(self, request, view):
        # Must pass accounting admin first
        if not super().has_permission(request, view):
            return False

        user = request.user
        role = getattr(user, "role", None)
        if not role:
            return False

        apps = role.apps or {}
        accounting = apps.get("accounting")

        if not isinstance(accounting, dict):
            return False

        permissions = accounting.get("permissions", [])
        return self.action_permission in permissions
    

class IsAccountingViewer(BaseAccessPolicy):
    """
    Allows read-only access to accounting data
    (ledger, reports, balances).
    """

    domain = "accounting"
    min_level = (
        "viewer",
        "staff",
        "manager",
        "admin",
        "superadmin",
    )