# verticals/ustadzku/permissions.py

from core.permissions.registry import PermissionRegistry


USTADZKU_PERMISSIONS = [

    # =========================
    # DASHBOARD
    # =========================
    {
        "module": "ustadzku",
        "code": "ustadzku.dashboard.view",
        "description": "View Ustadzku dashboard",
    },

    # =========================
    # PROFILE
    # =========================
    {
        "module": "ustadzku",
        "code": "ustadzku.profile.view",
        "description": "View own profile",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.profile.update",
        "description": "Update own profile",
    },

    # =========================
    # BOOKINGS
    # =========================
    {
        "module": "ustadzku",
        "code": "ustadzku.bookings.view",
        "description": "View bookings",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.bookings.create",
        "description": "Create booking",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.bookings.cancel",
        "description": "Cancel booking",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.bookings.approve",
        "description": "Approve booking (Ustadz)",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.bookings.reject",
        "description": "Reject booking (Ustadz)",
    },

    # =========================
    # SCHEDULE
    # =========================
    {
        "module": "ustadzku",
        "code": "ustadzku.schedule.view",
        "description": "View teaching schedule",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.schedule.manage",
        "description": "Manage teaching schedule",
    },

    # =========================
    # REVIEWS
    # =========================
    {
        "module": "ustadzku",
        "code": "ustadzku.reviews.view",
        "description": "View reviews",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.reviews.create",
        "description": "Create review",
    },

    # =========================
    # WALLET / PAYOUT
    # =========================
    {
        "module": "ustadzku",
        "code": "ustadzku.wallet.view",
        "description": "View wallet balance",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.payout.request",
        "description": "Request payout",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.payout.approve",
        "description": "Approve payout (Admin)",
    },

    # =========================
    # ADMIN MANAGEMENT
    # =========================
    {
        "module": "ustadzku",
        "code": "ustadzku.users.manage",
        "description": "Manage users (Admin)",
    },
    {
        "module": "ustadzku",
        "code": "ustadzku.settings.manage",
        "description": "Manage Ustadzku settings",
    },
]


# Register ke PermissionRegistry
PermissionRegistry.register(USTADZKU_PERMISSIONS)
