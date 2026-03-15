# verticals/hrms/seeds/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.hrms.enum.permissions import HrmsPermission
from core.roles.enums import RoleCode


ROLES = [

    # 🔥 HR Administrator (Full HR Control)
    {
        "code": RoleCode.ADMIN,
        "name": "HR Administrator",
        "description": "Full control over HRMS configuration and operations",
        "access_level": 100,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            HrmsPermission.ADMIN_DASHBOARD_VIEW, 
        ],
    },


    # 👑 Executive (Strategic Monitoring)
    {
        "code": RoleCode.DIRECTOR,
        "name": "Executive",
        "description": "Strategic oversight of workforce and payroll",
        "access_level": 90,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            HrmsPermission.EXECUTIVE_DASHBOARD_VIEW,
        ],
    },


    # 💰 Finance Officer (Payroll & Journal)
    {
        "code": RoleCode.FINANCE,
        "name": "Finance Officer",
        "description": "Manage payroll processing and accounting integration",
        "access_level": 80,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            HrmsPermission.FINANCE_DASHBOARD_VIEW,
        ],
    },


    # 🧾 HR Officer (Daily HR Operations)
    {
        "code": RoleCode.ADMIN,
        "name": "HR Officer",
        "description": "Handle daily HR operational activities",
        "access_level": 70,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            HrmsPermission.OFFICER_DASHBOARD_VIEW,
        ],
    },


    # 👨‍💼 Line Manager (Team-Level Control)
    {
        "code": RoleCode.MANAGER,
        "name": "Line Manager",
        "description": "Manage team members and approve requests",
        "access_level": 60,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            HrmsPermission.LINE_MANAGER_DASHBOARD_VIEW, 
        ],
    },


    # 👤 Employee (Self-Service User)
    {
        "code": RoleCode.CUSTOMER,
        "name": "Employee",
        "description": "Self-service access to personal HR data",
        "access_level": 40,
        "default_permissions": [

            CorePermission.DASHBOARD_VIEW,

            HrmsPermission.EMPLOYEE_DASHBOARD_VIEW,
        ],
    },

]