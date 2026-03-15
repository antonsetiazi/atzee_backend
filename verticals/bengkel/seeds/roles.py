# verticals/bengkel/seeds/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
from verticals.bengkel.enum.permissions import BengkelPermission
from core.roles.enums import RoleCode


ROLES = [

    # 🔥 Owner (Full Tenant Control)
    {
        "code": RoleCode.OWNER,
        "name": "Owner",
        "description": "Tenant owner with full control over workshop operations",
        "access_level": 100,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Bengkel
            BengkelPermission.OWNER_DASHBOARD_VIEW,
        ],
    },


    # 🛠 Service Advisor
    {
        "code": RoleCode.ADVISOR,
        "name": "Service Advisor",
        "description": "Manage work orders, customer service, and approvals",
        "access_level": 70,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # # Bengkel
            BengkelPermission.SERVICE_ADVISOR_DASHBOARD_VIEW,
        ],
    },


    # 🔧 Mechanic
    {
        "code": RoleCode.TECHNICIAN,
        "name": "Mechanic",
        "description": "Handle assigned jobs and update job progress",
        "access_level": 40,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Bengkel
            BengkelPermission.MECHANIC_DASHBOARD_VIEW,
        ],
    },


    # 💰 Cashier
    {
        "code": RoleCode.CASHIER,
        "name": "Cashier",
        "description": "Handle invoice and payment processing",
        "access_level": 50,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # Bengkel
            BengkelPermission.CASHIER_DASHBOARD_VIEW,
        ],
    },
]