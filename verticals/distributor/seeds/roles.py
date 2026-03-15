# verticals/distributor/seeds/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
from verticals.distributor.enum.permissions import DistributorPermission
from core.roles.enums import RoleCode


ROLES = [

    # ======================================================
    # 👑 OWNER (FULL TENANT CONTROL)
    # ======================================================
    {
        "code": RoleCode.OWNER,
        "name": "Owner",
        "description": "Tenant owner with full control over Distributor ERP",
        "access_level": 100,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # Distributor
            DistributorPermission.EXECUTIVE_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 🧠 GENERAL MANAGER
    # ======================================================
    {
        "code": RoleCode.GM,
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
        "code": RoleCode.MANAGER,
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
        "code": RoleCode.WAREHOUSE,
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
        "code": RoleCode.FINANCE,
        "name": "Finance Manager",
        "description": "Oversee receivable, payment, and financial reports",
        "access_level": 75,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.FINANCE_MANAGER_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 🧾 ADMIN SALES
    # ======================================================
    {
        "code": RoleCode.ADMIN,
        "name": "Admin Sales",
        "description": "Handle sales order entry and invoice processing",
        "access_level": 55,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.ADMIN_SALES_DASHBOARD_VIEW,
        ],
    },

    # ======================================================
    # 💵 FINANCE STAFF
    # ======================================================
    {
        "code": RoleCode.FINANCE,
        "name": "Finance Staff",
        "description": "Handle payment entry and invoice recording",
        "access_level": 45,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            DistributorPermission.FINANCE_STAFF_DASHBOARD_VIEW,
        ],
    },
]