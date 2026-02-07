# verticals/apotek/permissions/accounting.py

from core.permissions.access.accounting import IsAccountingAdmin


class IsApotekAccountingAdmin(IsAccountingAdmin):
    """
    Accounting access for Apotek vertical.
    """

    # Optional override
    # domain = "accounting"
    # min_level = ("manager", "admin")

    def has_permission(self, request, view):
        # First: must pass global accounting rules
        if not super().has_permission(request, view):
            return False

        # Vertical-specific rule (optional)
        user = request.user

        # Example: apotek flag / profile
        if not hasattr(user, "apotek_profile"):
            return False

        return True
