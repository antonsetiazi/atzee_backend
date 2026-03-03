# verticals/bengkel/seeds/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
# from verticals.bengkel.enum.permissions import BengkelPermission


ROLES = [

    # 🔥 Owner (Full Tenant Control)
    {
        "name": "Owner",
        "description": "Tenant owner with full control over workshop operations",
        "access_level": 100,
        "auto_assign": "owner",
    },


    # 🛠 Service Advisor
    {
        "name": "Service Advisor",
        "description": "Manage work orders, customer service, and approvals",
        "access_level": 70,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # # Bengkel
            # BengkelPermission.DASHBOARD_VIEW,
            # BengkelPermission.WORK_ORDER_VIEW,
            # BengkelPermission.WORK_ORDER_CREATE,
            # BengkelPermission.WORK_ORDER_UPDATE,
            # BengkelPermission.WORK_ORDER_APPROVE,
            # BengkelPermission.VEHICLE_VIEW,
            # BengkelPermission.VEHICLE_CREATE,
            # BengkelPermission.APPOINTMENT_VIEW,
            # BengkelPermission.APPOINTMENT_CREATE,

            # # Business
            # BusinessPermission.CUSTOMERS_VIEW,
            # BusinessPermission.CUSTOMERS_CREATE,
            # BusinessPermission.PRODUCTS_VIEW,
            # BusinessPermission.INVENTORY_VIEW,
        ],
    },


    # 🔧 Mechanic
    {
        "name": "Mechanic",
        "description": "Handle assigned jobs and update job progress",
        "access_level": 40,
        "default_permissions": [

            # Bengkel
            # BengkelPermission.MY_JOB_VIEW,
            # BengkelPermission.WORK_ORDER_UPDATE_STATUS,
            # BengkelPermission.CHECKLIST_UPDATE,
            # BengkelPermission.PARTS_REQUEST_CREATE,

            # # Business
            # BusinessPermission.PRODUCTS_VIEW,
        ],
    },


    # 💰 Cashier
    {
        "name": "Cashier",
        "description": "Handle invoice and payment processing",
        "access_level": 50,
        "default_permissions": [

            # Core
            CorePermission.DASHBOARD_VIEW,

            # # Bengkel
            # BengkelPermission.WORK_ORDER_DONE_VIEW,
            # BengkelPermission.DAILY_CLOSING_VIEW,

            # # Business
            # BusinessPermission.TRANSACTION_VIEW,
            # BusinessPermission.TRANSACTION_CREATE,
            # BusinessPermission.PAYMENT_CREATE,
        ],
    },
]