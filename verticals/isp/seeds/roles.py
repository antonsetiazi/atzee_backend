# verticals/isp/roles.py

from core.enum.permissions import CorePermission
# from business.enum.permissions import BusinessPermission
from verticals.isp.enum.permissions import IspPermission


ROLES = [

    # 🔥 100 - Owner (Full ISP Control)
    {
        "name": "Owner",
        "description": "Full control over ISP tenant including finance and network infrastructure",
        "access_level": 100,
        "auto_assign": "owner",
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.OWNER_DASHBOARD_VIEW,
        ],
    },


    # 🏢 90 - General Manager
    {
        "name": "General Manager",
        "description": "Manage overall ISP operations, customers, billing and monitoring",
        "access_level": 90,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.GM_DASHBOARD_VIEW,
        ],
    },


    # 💳 80 - Finance Manager
    {
        "name": "Finance Manager",
        "description": "Manage ISP financial operations and reporting",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.FINANCE_DASHBOARD_VIEW,
        ],
    },


    # 🧠 70 - Network Engineer
    {
        "name": "Network Engineer",
        "description": "Manage network devices, IP pools, bandwidth and provisioning",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.NETWORK_DASHBOARD_VIEW,
        ],
    },


    # 🖥 60 - NOC Staff
    {
        "name": "NOC Staff",
        "description": "Monitor network health and handle technical incidents",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.NOC_DASHBOARD_VIEW,
        ],
    },


    # 💰 50 - Billing Staff
    {
        "name": "Billing Staff",
        "description": "Handle invoicing, payments and overdue accounts",
        "access_level": 50,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.BILLING_DASHBOARD_VIEW,
        ],
    },


    # 📞 40 - Customer Service
    {
        "name": "Customer Service",
        "description": "Handle customer inquiries and trouble tickets",
        "access_level": 40,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.CS_DASHBOARD_VIEW,
        ],
    },


    # 📈 30 - Sales Marketing
    {
        "name": "Sales Marketing",
        "description": "Manage leads, sales orders and promotions",
        "access_level": 30,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.SALES_DASHBOARD_VIEW,
        ],
    },


    # 🔧 20 - Field Technician
    {
        "name": "Field Technician",
        "description": "Handle installations and on-site troubleshooting",
        "access_level": 20,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.FIELD_DASHBOARD_VIEW,
        ],
    },


    # 🌐 10 - Customer (Portal)
    {
        "name": "Customer",
        "description": "Self-service portal for ISP subscribers",
        "access_level": 10,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            IspPermission.CUSTOMER_PORTAL_VIEW,
        ],
    },

]