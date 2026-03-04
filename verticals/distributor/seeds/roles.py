# verticals/distributor/seeds/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
from verticals.distributor.enum.permissions import DistributorPermission


ROLES = [

    # ======================================================
    # 👑 OWNER (FULL TENANT CONTROL)
    # ======================================================
    {
        "name": "Owner",
        "description": "Tenant owner with full control over Distributor ERP",
        "access_level": 100,
        "auto_assign": "owner",
    },

    # ======================================================
    # 🧠 GENERAL MANAGER
    # ======================================================
    {
        "name": "General Manager",
        "description": "Oversee overall distributor operations",
        "access_level": 90,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # Distributor
            DistributorPermission.EXECUTIVE_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 📊 SALES MANAGER
    # ======================================================
    {
        "name": "Sales Manager",
        "description": "Manage sales team, territory, and sales performance",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.SALES_MANAGER_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 📦 WAREHOUSE MANAGER
    # ======================================================
    {
        "name": "Warehouse Manager",
        "description": "Manage warehouse and stock operations",
        "access_level": 75,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.WAREHOUSE_MANAGER_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 💰 FINANCE MANAGER
    # ======================================================
    {
        "name": "Finance Manager",
        "description": "Oversee receivable, payment, and financial reports",
        "access_level": 75,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.FINANCE_MANAGER_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 🚚 SALES REP (FIELD)
    # ======================================================
    {
        "name": "Sales Rep",
        "description": "Field sales representative handling customer orders",
        "access_level": 50,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.SALES_REP_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 🧾 ADMIN SALES
    # ======================================================
    {
        "name": "Admin Sales",
        "description": "Handle sales order entry and invoice processing",
        "access_level": 55,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.ADMIN_SALES_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 📦 WAREHOUSE STAFF
    # ======================================================
    {
        "name": "Warehouse Staff",
        "description": "Handle goods receipt and delivery processing",
        "access_level": 45,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.WAREHOUSE_STAFF_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 💵 FINANCE STAFF
    # ======================================================
    {
        "name": "Finance Staff",
        "description": "Handle payment entry and invoice recording",
        "access_level": 45,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.FINANCE_STAFF_DASHBOARD_VIEW,
        ],
    },
]