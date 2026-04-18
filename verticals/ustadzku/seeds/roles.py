# verticals/ustadzku/seeds/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from marketplace.enum.permissions import MarketplacePermission
from verticals.ustadzku.enum.permissions import UstadzkuPermission
from core.roles.enums import RoleCode


ROLES = [
    {
        "code": RoleCode.GUEST,
        "name": "Guest",
        "description": "Public visitor (not authenticated)",
        "access_level": 0,
        "default_permissions": [
            UstadzkuPermission.GUEST_HOME_VIEW,
        ],
    },

    # Tenant Owner / Superadmin lokal tenant
    {
        "code": RoleCode.OWNER,
        "name": "Owner",
        "description": "Tenant owner, full control over tenant",
        "access_level": 100,
        "auto_assign": "owner",
    },

    # Admin tenant: manage users, roles, settings
    {
        "code": RoleCode.ADMIN,
        "name": "Admin",
        "description": "Manage users, roles, and tenant settings",
        "access_level": 80,
        "default_permissions": [
            CorePermission.DASHBOARD_VIEW,
            CorePermission.ADMIN_USERS_VIEW,
            CorePermission.ADMIN_WALLET_TRANSACTIONS_VIEW,
            CorePermission.ADMIN_WALLET_WITHDRAWAL_VIEW,
            CorePermission.ADMIN_WIDGETS_VIEW,
            BusinessPermission.ADMIN_BOOKINGS_VIEW,
            BusinessPermission.ADMIN_PAYMENT_GATEWAY_VIEW,
            UstadzkuPermission.ADMIN_DASHBOARD_VIEW,
            BusinessPermission.PARTNERS_CREATE,
            BusinessPermission.PARTNERS_UPDATE,
            BusinessPermission.PARTNERS_VIEW,
            BusinessPermission.USERS_VIEW,
            BusinessPermission.ADMIN_REVIEWS_VIEW,
            MarketplacePermission.ADMIN_ORDERS_VIEW,
        ],
    },

    # Staff: operational role, internal user
    {
        "code": RoleCode.STAFF,
        "name": "Staff",
        "description": "Internal staff access for operations",
        "access_level": 40,
        "default_permissions": [
            CorePermission.DASHBOARD_VIEW,
        ],
    },

    # Customer / Pelanggan: user eksternal yang membeli layanan
    {
        "code": RoleCode.CUSTOMER,
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
            # BusinessPermission.BOOKINGS_CREATE,
            # BusinessPermission.BOOKINGS_VIEW,
            # BusinessPermission.BOOKINGS_PAY,
            BusinessPermission.PARTNERS_VIEW,
            # BusinessPermission.USER_BOOKINGS_VIEW,
            UstadzkuPermission.USER_DASHBOARD_VIEW,
        ],
    },

    # Partner / Seller: user eksternal yang menjual produk/jasa via tenant
    {
        "code": RoleCode.PARTNER,
        "name": "Partner",
        "description": "External partner or seller of the tenant",
        "access_level": 5,
        "default_permissions": [
            CorePermission.ACCOUNT_PASSWORD_UPDATE,
            CorePermission.ACCOUNT_PROFILE_VIEW,
            CorePermission.ACCOUNT_PROFILE_UPDATE,
            CorePermission.DASHBOARD_VIEW,
            CorePermission.NOTIFICATION_VIEW,
            CorePermission.CATEGORIES_VIEW,
            CorePermission.FILES_VIEW,
            
            BusinessPermission.PARTNERS_VIEW,
            BusinessPermission.PARTNERS_PORTAL,
            BusinessPermission.PARTNERS_PORTAL_UPDATE,
            # BusinessPermission.PARTNER_BOOKINGS_VIEW,

            MarketplacePermission.PARTNER_PRODUCTS_VIEW,
            MarketplacePermission.PARTNER_PRODUCTS_EDIT,
            MarketplacePermission.PARTNER_PRODUCTS_CREATE,
            
            UstadzkuPermission.PARTNER_DASHBOARD_VIEW,
        ],
    },
]
