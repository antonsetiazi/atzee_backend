# verticals/hrms/seeds/roles.py

from core.enum.permissions import CorePermission
from business.enum.permissions import BusinessPermission
from verticals.hrms.enum.permissions import HRMSPermission


ROLES = [

    # 🔥 HR Administrator (Full HR Control)
    {
        "name": "HR Administrator",
        "description": "Full control over HRMS configuration and operations",
        "access_level": 100,
        "default_permissions": [

            # CorePermission.DASHBOARD_VIEW,

            # Organization
            # HRMSPermission.ORGANIZATION_VIEW, 
            # HRMSPermission.ORGANIZATION_MANAGE,

            # Employees
            # HRMSPermission.EMPLOYEE_VIEW,  
            # HRMSPermission.EMPLOYEE_CREATE, 
            # HRMSPermission.EMPLOYEE_UPDATE,
            # HRMSPermission.EMPLOYEE_DELETE, 

            # Attendance
            # HRMSPermission.ATTENDANCE_VIEW,
            # HRMSPermission.ATTENDANCE_MANAGE,  

            # Leave
            # HRMSPermission.LEAVE_VIEW,  
            # HRMSPermission.LEAVE_APPROVE,

            # Payroll
            # HRMSPermission.PAYROLL_VIEW, 
            # HRMSPermission.PAYROLL_GENERATE,
            # HRMSPermission.PAYROLL_APPROVE,

            # Performance
            # HRMSPermission.PERFORMANCE_VIEW, 
            # HRMSPermission.PERFORMANCE_MANAGE,

            # Reports
            # HRMSPermission.REPORT_VIEW, 
        ],
    },


    # 👑 Executive (Strategic Monitoring)
    {
        "name": "Executive",
        "description": "Strategic oversight of workforce and payroll",
        "access_level": 90,
        "default_permissions": [

            # CorePermission.DASHBOARD_VIEW,

            # HRMSPermission.EXECUTIVE_DASHBOARD_VIEW,
            # HRMSPermission.EMPLOYEE_VIEW,
            # HRMSPermission.PAYROLL_VIEW,
            # HRMSPermission.REPORT_VIEW,
        ],
    },


    # 💰 Finance Officer (Payroll & Journal)
    {
        "name": "Finance Officer",
        "description": "Manage payroll processing and accounting integration",
        "access_level": 80,
        "default_permissions": [

            # CorePermission.DASHBOARD_VIEW,

            # HRMSPermission.PAYROLL_VIEW,
            # HRMSPermission.PAYROLL_GENERATE,
            # HRMSPermission.PAYROLL_APPROVE,

            # HRMSPermission.PAYROLL_JOURNAL_POST, 
            # HRMSPermission.REPORT_VIEW,
        ],
    },


    # 🧾 HR Officer (Daily HR Operations)
    {
        "name": "HR Officer",
        "description": "Handle daily HR operational activities",
        "access_level": 70,
        "default_permissions": [

            # CorePermission.DASHBOARD_VIEW,

            # HRMSPermission.EMPLOYEE_VIEW,
            # HRMSPermission.EMPLOYEE_CREATE,
            # HRMSPermission.EMPLOYEE_UPDATE,

            # HRMSPermission.ATTENDANCE_VIEW,
            # HRMSPermission.ATTENDANCE_MANAGE,

            # HRMSPermission.LEAVE_VIEW,
            # HRMSPermission.LEAVE_APPROVE,

            # HRMSPermission.PAYROLL_VIEW,
            # HRMSPermission.REPORT_VIEW,
        ],
    },


    # 👨‍💼 Line Manager (Team-Level Control)
    {
        "name": "Line Manager",
        "description": "Manage team members and approve requests",
        "access_level": 60,
        "default_permissions": [

            # CorePermission.DASHBOARD_VIEW,

            # HRMSPermission.TEAM_DASHBOARD_VIEW, 
            # HRMSPermission.TEAM_MEMBER_VIEW,

            # HRMSPermission.ATTENDANCE_VIEW,

            # HRMSPermission.LEAVE_VIEW,
            # HRMSPermission.LEAVE_APPROVE,

            # HRMSPermission.PERFORMANCE_VIEW,
        ],
    },


    # 👤 Employee (Self-Service User)
    {
        "name": "Employee",
        "description": "Self-service access to personal HR data",
        "access_level": 40,
        "default_permissions": [

            # CorePermission.DASHBOARD_VIEW,

            # HRMSPermission.MY_PROFILE_VIEW,
            # HRMSPermission.MY_ATTENDANCE_VIEW,
            # HRMSPermission.MY_LEAVE_REQUEST,
            # HRMSPermission.MY_PAYROLL_VIEW,
            # HRMSPermission.MY_PERFORMANCE_VIEW,
        ],
    },

]