# verticals/marketplace/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.marketplace.enum.permissions import MarketplacePermission
from core.roles.enums import RoleCode

ROLES = [

    # 👑 Marketplace Admin (Platform Control)
    {
        "code": RoleCode.ADMIN,
        "name": "Admin",
        "description": "Marketplace administrator with full control over platform operations",
        "access_level": 100,
        "auto_assign": "admin",
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Marketplace
            MarketplacePermission.ADMIN_DASHBOARD_VIEW,
        ],
    },


    # 🏪 Seller (Store Owner)
    {
        "code": RoleCode.PARTNER,
        "name": "Seller",
        "description": "Manage store, products, orders and sales performance",
        "access_level": 70,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Marketplace
            MarketplacePermission.SELLER_DASHBOARD_VIEW,
        ],
    },


    # 🛒 Buyer (Customer)
    {
        "code": RoleCode.CUSTOMER,
        "name": "Buyer",
        "description": "Browse products, place orders and manage purchases",
        "access_level": 20,
        "auto_assign": "buyer",
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Marketplace
            MarketplacePermission.BUYER_DASHBOARD_VIEW,
        ],
    },
]