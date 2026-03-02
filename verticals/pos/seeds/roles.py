# verticals/pos/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.pos.enum.permissions import PosPermission


ROLES = [

    # 🔥 Owner (Full tenant control)
    {
        "name": "Owner",
        "description": "Tenant owner with full control over POS operations",
        "access_level": 100,
        "auto_assign": "owner",
    },


    # 🏬 Store Manager
    {
        "name": "Manager",
        "description": "Manage store operations, reports, and staff",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # POS Core
            PosPermission.MANAGER_DASHBOARD_VIEW,
            # PosPermission.TRANSACTION_VIEW,
            # PosPermission.TRANSACTION_REFUND,
            # PosPermission.SHIFT_MANAGE,
            # PosPermission.REPORT_VIEW,
            # PosPermission.OUTLET_SETTINGS_VIEW,

            # Business
            BusinessPermission.PRODUCTS_VIEW, 
            BusinessPermission.INVENTORY_VIEW,
            BusinessPermission.CUSTOMERS_VIEW,
        ],
    },
 

    # 👨‍💼 Shift Supervisor
    {
        "name": "Supervisor",
        "description": "Supervise cashier and manage shifts",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,
 
            PosPermission.SUPERVISOR_DASHBOARD_VIEW,
            # PosPermission.TRANSACTION_VIEW,
            # PosPermission.TRANSACTION_CREATE,
            # PosPermission.TRANSACTION_REFUND,
            # PosPermission.SHIFT_OPEN,
            # PosPermission.SHIFT_CLOSE,
            # PosPermission.REPORT_VIEW,
        ],
    },


    # 🧾 Cashier
    {
        "name": "Cashier",
        "description": "Handle daily POS transactions",
        "access_level": 40,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,
            PosPermission.CASHIER_DASHBOARD_VIEW, 
            PosPermission.TRANSACTION_CASHIER_CREATE,
            # PosPermission.TRANSACTION_VIEW,
            # PosPermission.SHIFT_OPEN,
        ],
    },


    # 🌍 Area Manager (Multi Outlet Monitoring)
    {
        "name": "Area Manager",
        "description": "Monitor multiple outlets performance",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            PosPermission.AREA_DASHBOARD_VIEW,
            # PosPermission.REPORT_VIEW,
            # PosPermission.OUTLET_PERFORMANCE_VIEW,
        ],
    },
]