# verticals/ustadzku/seeds/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.ustadzku.enum.permissions import UstadzkuPermission

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
            CorePermission.DASHBOARD_VIEW,
            BusinessPermission.ADMIN_BOOKINGS_VIEW,
            UstadzkuPermission.ADMIN_DASHBOARD_VIEW,
            BusinessPermission.PARTNERS_CREATE,
            BusinessPermission.PARTNERS_UPDATE,
            BusinessPermission.PARTNERS_VIEW,
            BusinessPermission.USERS_VIEW,
        ],
    },

    # Staff: operational role, internal user
    {
        "name": "Staff",
        "description": "Internal staff access for operations",
        "access_level": 40,
        "default_permissions": [
            CorePermission.DASHBOARD_VIEW,
        ],
    },

    # Viewer: read-only internal role
    {
        "name": "Viewer",
        "description": "Read-only access to internal tenant data",
        "access_level": 10,
        "default_permissions": [
            CorePermission.DASHBOARD_VIEW,
        ],
    },

    # Customer / Pelanggan: user eksternal yang membeli layanan
    {
        "name": "Customer",
        "description": "External customer / client of the tenant",
        "access_level": 5,
        "default_permissions": [
            CorePermission.ACCOUNT_ADDRESS_CREATE,
            CorePermission.ACCOUNT_ADDRESS_UPDATE,
            CorePermission.ACCOUNT_PASSWORD_UPDATE,
            CorePermission.ACCOUNT_PROFILE_VIEW,
            CorePermission.ACCOUNT_PROFILE_UPDATE,
            CorePermission.ACCOUNT_SETTINGS_VIEW,
            CorePermission.ACCOUNT_SETTINGS_UPDATE,
            CorePermission.CLASSIFICATIONS_TAGS_VIEW,
            CorePermission.DASHBOARD_VIEW,
            CorePermission.FILES_VIEW,
            CorePermission.GEO_SPATIAL_VIEW,
            CorePermission.NOTIFICATION_VIEW,
            CorePermission.TAGS_VIEW,
            CorePermission.TIMEZONES_VIEW,
            CorePermission.USER_WALLET_VIEW,
            BusinessPermission.BOOKINGS_CREATE,
            BusinessPermission.BOOKINGS_VIEW,
            BusinessPermission.BOOKINGS_PAY,
            BusinessPermission.PARTNERS_VIEW,
            BusinessPermission.USER_BOOKINGS_VIEW,
            UstadzkuPermission.USER_DASHBOARD_VIEW,
        ],
    },

    # Partner / Seller: user eksternal yang menjual produk/jasa via tenant
    {
        "name": "Partner",
        "description": "External partner or seller of the tenant",
        "access_level": 5,
        "default_permissions": [
            CorePermission.ACCOUNT_PASSWORD_UPDATE,
            CorePermission.ACCOUNT_PROFILE_VIEW,
            CorePermission.ACCOUNT_PROFILE_UPDATE,
            CorePermission.DASHBOARD_VIEW,
            CorePermission.NOTIFICATION_VIEW,
            BusinessPermission.PARTNERS_VIEW,
            BusinessPermission.PARTNER_BOOKINGS_VIEW,
            UstadzkuPermission.PARTNER_DASHBOARD_VIEW,
        ],
    },
]
