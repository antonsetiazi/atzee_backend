# verticals/isp/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
# from verticals.isp.enum.permissions import IspPermission


ROLES = [

    # 🔥 100 - Owner (Full ISP Control)
    {
        "name": "Owner",
        "description": "Full control over ISP tenant including finance and network infrastructure",
        "access_level": 100,
        "auto_assign": "owner",
    },


    # 🏢 90 - General Manager
    {
        "name": "General Manager",
        "description": "Manage overall ISP operations, customers, billing and monitoring",
        "access_level": 90,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # # Business
            # BusinessPermission.CUSTOMERS_VIEW,
            # BusinessPermission.SUBSCRIPTIONS_VIEW,
            # BusinessPermission.INVOICES_VIEW,
            # BusinessPermission.PAYMENTS_VIEW,

            # # ISP
            # IspPermission.DASHBOARD_VIEW,
            # IspPermission.MONITORING_VIEW,
            # IspPermission.REPORT_VIEW,
        ],
    },


    # 💳 80 - Finance Manager
    {
        "name": "Finance Manager",
        "description": "Manage ISP financial operations and reporting",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # # Business
            # BusinessPermission.INVOICES_VIEW,
            # BusinessPermission.PAYMENTS_VIEW,
            # BusinessPermission.FINANCIAL_REPORT_VIEW,

            # # ISP
            # IspPermission.FINANCIAL_REPORT_VIEW,
        ],
    },


    # 🧠 70 - Network Engineer
    {
        "name": "Network Engineer",
        "description": "Manage network devices, IP pools, bandwidth and provisioning",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # ISP Core Network
            # IspPermission.DEVICE_VIEW,
            # IspPermission.DEVICE_MANAGE,
            # IspPermission.IP_POOL_VIEW,
            # IspPermission.IP_POOL_MANAGE,
            # IspPermission.BANDWIDTH_PROFILE_VIEW,
            # IspPermission.BANDWIDTH_PROFILE_MANAGE,
            # IspPermission.MONITORING_VIEW,
        ],
    },


    # 🖥 60 - NOC Staff
    {
        "name": "NOC Staff",
        "description": "Monitor network health and handle technical incidents",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # IspPermission.MONITORING_VIEW,
            # IspPermission.ACTIVE_SESSION_VIEW,
            # IspPermission.SESSION_RESTART,
            # IspPermission.TICKET_VIEW,
            # IspPermission.TICKET_CREATE,
        ],
    },


    # 💰 50 - Billing Staff
    {
        "name": "Billing Staff",
        "description": "Handle invoicing, payments and overdue accounts",
        "access_level": 50,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # # Business Billing
            # BusinessPermission.INVOICES_VIEW,
            # BusinessPermission.INVOICES_MANAGE,
            # BusinessPermission.PAYMENTS_VIEW,
            # BusinessPermission.PAYMENTS_MANAGE,

            # # ISP Billing
            # IspPermission.OVERDUE_VIEW,
        ],
    },


    # 📞 40 - Customer Service
    {
        "name": "Customer Service",
        "description": "Handle customer inquiries and trouble tickets",
        "access_level": 40,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # BusinessPermission.CUSTOMERS_VIEW,
            # BusinessPermission.SUBSCRIPTIONS_VIEW,

            # IspPermission.TICKET_VIEW,
            # IspPermission.TICKET_CREATE,
            # IspPermission.INSTALLATION_VIEW,
        ],
    },


    # 📈 30 - Sales Marketing
    {
        "name": "Sales Marketing",
        "description": "Manage leads, sales orders and promotions",
        "access_level": 30,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            # IspPermission.LEAD_VIEW,
            # IspPermission.LEAD_CREATE,
            # IspPermission.SALES_ORDER_VIEW,
            # IspPermission.SALES_ORDER_CREATE,
            # IspPermission.COMMISSION_VIEW,
        ],
    },


    # 🔧 20 - Field Technician
    {
        "name": "Field Technician",
        "description": "Handle installations and on-site troubleshooting",
        "access_level": 20,
        "default_permissions": [

            # IspPermission.MY_TASK_VIEW,
            # IspPermission.INSTALLATION_VIEW,
            # IspPermission.INSTALLATION_UPDATE,
            # IspPermission.TICKET_VIEW,
        ],
    },


    # 🌐 10 - Customer (Portal)
    {
        "name": "Customer",
        "description": "Self-service portal for ISP subscribers",
        "access_level": 10,
        "default_permissions": [

            # IspPermission.PORTAL_DASHBOARD_VIEW,
            # IspPermission.MY_SUBSCRIPTION_VIEW,
            # IspPermission.MY_INVOICE_VIEW,
            # IspPermission.MY_TICKET_VIEW,
            # IspPermission.MY_TICKET_CREATE,
        ],
    },

]