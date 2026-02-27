# verticals/ustadzku/roles.py

ROLES = [
    # Tenant Owner / Superadmin lokal tenant
    {
        "name": "Owner",
        "description": "Tenant owner, full control over tenant",
        "access_level": 100,
        "auto_assign": "owner",
    },

    # Admin tenant: manage users, roles, settings
    {
        "name": "Admin",
        "description": "Manage users, roles, and tenant settings",
        "access_level": 80,
        "default_permissions": [
            "core.dashboard.view",
            "ustadzku.dashboard.view",
        ],
    },

    # Staff: operational role, internal user
    {
        "name": "Staff",
        "description": "Internal staff access for operations",
        "access_level": 40,
        "default_permissions": [
            "core.dashboard.view",
            "ustadzku.dashboard.view",
            "business.partners.view",
        ],
    },

    # Viewer: read-only internal role
    {
        "name": "Viewer",
        "description": "Read-only access to internal tenant data",
        "access_level": 10,
        "default_permissions": [
            "core.dashboard.view",
            "ustadzku.dashboard.view",
        ],
    },

    # Customer / Pelanggan: user eksternal yang membeli layanan
    {
        "name": "Customer",
        "description": "External customer / client of the tenant",
        "access_level": 5,
        "default_permissions": [
            "core.account.profile.view",
            "core.account.profile.update",
            "core.account.settings.view",
            "core.account.settings.update",
            "core.account.password.update",
            "core.dashboard.view",
            "ustadzku.user.dashboard.view",
            "business.user.bookings.view",
            "business.partners.view",
            "business.bookings.create",
            "business.bookings.view",
            "business.bookings.pay",
            "core.files.view",
            "core.tags.view",
            "core.classifications.tags.view",
            "core.user.wallet.view",
            "core.timezones.view",
            "core.notification.view",
        ],
    },

    # Partner / Seller: user eksternal yang menjual produk/jasa via tenant
    {
        "name": "Partner",
        "description": "External partner or seller of the tenant",
        "access_level": 5,
        "default_permissions": [
            "core.dashboard.view",
            "ustadzku.partner.dashboard.view",
            "business.partners.view",
        ],
    },
]
