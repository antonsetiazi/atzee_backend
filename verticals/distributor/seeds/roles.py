# verticals/distributor/seeds/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
# from verticals.distributor.enum.permissions import DistributorPermission


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

            # # Distributor
            # DistributorPermission.GLOBAL_DASHBOARD_VIEW,
            # DistributorPermission.REPORT_VIEW,

            # # Business
            # BusinessPermission.PRODUCTS_VIEW,
            # BusinessPermission.INVENTORY_VIEW,
            # BusinessPermission.CUSTOMERS_VIEW,
            # BusinessPermission.SUPPLIERS_VIEW,
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

            # DistributorPermission.SALES_DASHBOARD_VIEW,
            # DistributorPermission.SALES_ORDER_VIEW,
            # DistributorPermission.SALES_ORDER_CREATE,
            # DistributorPermission.SALES_RETURN_VIEW,
            # DistributorPermission.SALES_TARGET_VIEW,

            # BusinessPermission.CUSTOMERS_VIEW,
            # BusinessPermission.PRODUCTS_VIEW,
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

            # DistributorPermission.WAREHOUSE_DASHBOARD_VIEW,
            # DistributorPermission.GOODS_RECEIPT_VIEW,
            # DistributorPermission.DELIVERY_ORDER_VIEW,
            # DistributorPermission.STOCK_ADJUSTMENT,

            # BusinessPermission.INVENTORY_VIEW,
            # BusinessPermission.PRODUCTS_VIEW,
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

            # DistributorPermission.FINANCE_DASHBOARD_VIEW,
            # DistributorPermission.INVOICE_VIEW,
            # DistributorPermission.PAYMENT_VIEW,
            # DistributorPermission.AGING_REPORT_VIEW,

            # BusinessPermission.CUSTOMERS_VIEW,
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

            # DistributorPermission.SALESREP_DASHBOARD_VIEW,
            # DistributorPermission.SALES_ORDER_CREATE,
            # DistributorPermission.SALES_ORDER_VIEW,

            # BusinessPermission.CUSTOMERS_VIEW,
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

            # DistributorPermission.SALES_ORDER_VIEW,
            # DistributorPermission.SALES_ORDER_CREATE,
            # DistributorPermission.INVOICE_CREATE,
            # DistributorPermission.INVOICE_VIEW,

            # BusinessPermission.CUSTOMERS_VIEW,
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

            # DistributorPermission.GOODS_RECEIPT_VIEW,
            # DistributorPermission.DELIVERY_ORDER_VIEW,
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

            # DistributorPermission.PAYMENT_CREATE,
            # DistributorPermission.PAYMENT_VIEW,
            # DistributorPermission.INVOICE_VIEW,
        ],
    },
]