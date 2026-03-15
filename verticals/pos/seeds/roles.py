# verticals/pos/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.pos.enum.permissions import PosPermission
from core.roles.enums import RoleCode


ROLES = [

    # 🔥 Owner (Full tenant control)
    {
        "code": RoleCode.OWNER,
        "name": "Owner",
        "description": "Tenant owner with full control over POS operations",
        "access_level": 100,
        "auto_assign": "owner",
    },


    # 🏬 Store Manager
    {
        "code": RoleCode.MANAGER,
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
        "code": RoleCode.SUPERVISOR,
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
        "code": RoleCode.CASHIER,
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
        "code": RoleCode.MANAGER,
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