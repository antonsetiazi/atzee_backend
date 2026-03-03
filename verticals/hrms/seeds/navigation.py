# verticals/hrms/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — HR ADMINISTRATOR
    # ========================================
    {
        "tenant_code": None,
        "role": "HR Administrator",
        "type": "sidebar",
        "device": "desktop",
        "app": "hrms",
        "items": [
            {"action_type": "page", "target": "hrms.dashboard", "icon": "home", "route": "/hrms/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "hrms.organization", "icon": "layers", "route": "/hrms/organization", "label": "Organization"},
            {"action_type": "page", "target": "hrms.employees", "icon": "users", "route": "/hrms/employees", "label": "Employees"},
            {"action_type": "page", "target": "hrms.attendance", "icon": "clock", "route": "/hrms/attendance", "label": "Attendance"},
            {"action_type": "page", "target": "hrms.leave", "icon": "calendar", "route": "/hrms/leave", "label": "Leave Management"},
            {"action_type": "page", "target": "hrms.payroll", "icon": "dollar-sign", "route": "/hrms/payroll", "label": "Payroll"},
            {"action_type": "page", "target": "hrms.performance", "icon": "bar-chart-2", "route": "/hrms/performance", "label": "Performance"},
            {"action_type": "page", "target": "hrms.reports", "icon": "file-text", "route": "/hrms/reports", "label": "Reports"},
            {"action_type": "page", "target": "hrms.settings", "icon": "settings", "route": "/hrms/settings", "label": "Settings"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — HR OFFICER
    # ========================================
    {
        "tenant_code": None,
        "role": "HR Officer",
        "type": "sidebar",
        "device": "desktop",
        "app": "hrms",
        "items": [
            {"action_type": "page", "target": "hrms.dashboard", "icon": "home", "route": "/hrms/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "hrms.employees", "icon": "users", "route": "/hrms/employees", "label": "Employees"},
            {"action_type": "page", "target": "hrms.attendance", "icon": "clock", "route": "/hrms/attendance", "label": "Attendance"},
            {"action_type": "page", "target": "hrms.leave", "icon": "calendar", "route": "/hrms/leave", "label": "Leave Requests"},
            {"action_type": "page", "target": "hrms.payroll_process", "icon": "credit-card", "route": "/hrms/payroll/process", "label": "Payroll Processing"},
            {"action_type": "page", "target": "hrms.reports", "icon": "file-text", "route": "/hrms/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — LINE MANAGER
    # ========================================
    {
        "tenant_code": None,
        "role": "Line Manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "hrms",
        "items": [
            {"action_type": "page", "target": "hrms.team_dashboard", "icon": "activity", "route": "/hrms/team/dashboard", "label": "Team Dashboard"},
            {"action_type": "page", "target": "hrms.team_members", "icon": "users", "route": "/hrms/team/members", "label": "My Team"},
            {"action_type": "page", "target": "hrms.team_attendance", "icon": "clock", "route": "/hrms/team/attendance", "label": "Team Attendance"},
            {"action_type": "page", "target": "hrms.team_leave", "icon": "calendar", "route": "/hrms/team/leave", "label": "Leave Approvals"},
            {"action_type": "page", "target": "hrms.team_performance", "icon": "bar-chart-2", "route": "/hrms/team/performance", "label": "Performance Review"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — EMPLOYEE (SELF SERVICE)
    # ========================================
    {
        "tenant_code": None,
        "role": "Employee",
        "type": "sidebar",
        "device": "desktop",
        "app": "hrms",
        "items": [
            {"action_type": "page", "target": "hrms.my_dashboard", "icon": "home", "route": "/hrms/my/dashboard", "label": "My Dashboard"},
            {"action_type": "page", "target": "hrms.my_attendance", "icon": "clock", "route": "/hrms/my/attendance", "label": "My Attendance"},
            {"action_type": "page", "target": "hrms.my_leave", "icon": "calendar", "route": "/hrms/my/leave", "label": "My Leave"},
            {"action_type": "page", "target": "hrms.my_overtime", "icon": "plus-circle", "route": "/hrms/my/overtime", "label": "My Overtime"},
            {"action_type": "page", "target": "hrms.my_payroll", "icon": "dollar-sign", "route": "/hrms/my/payroll", "label": "My Payroll Slip"},
            {"action_type": "page", "target": "hrms.my_profile", "icon": "user", "route": "/hrms/my/profile", "label": "My Profile"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — FINANCE OFFICER
    # ========================================
    {
        "tenant_code": None,
        "role": "Finance Officer",
        "type": "sidebar",
        "device": "desktop",
        "app": "hrms",
        "items": [
            {"action_type": "page", "target": "hrms.payroll_dashboard", "icon": "home", "route": "/hrms/payroll/dashboard", "label": "Payroll Dashboard"},
            {"action_type": "page", "target": "hrms.payroll_period", "icon": "calendar", "route": "/hrms/payroll/period", "label": "Payroll Period"},
            {"action_type": "page", "target": "hrms.payroll_generate", "icon": "play-circle", "route": "/hrms/payroll/generate", "label": "Generate Payroll"},
            {"action_type": "page", "target": "hrms.payroll_journal", "icon": "book-open", "route": "/hrms/payroll/journal", "label": "Journal Posting"},
            {"action_type": "page", "target": "hrms.payroll_reports", "icon": "file-text", "route": "/hrms/payroll/reports", "label": "Payroll Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — EXECUTIVE
    # ========================================
    {
        "tenant_code": None,
        "role": "Executive",
        "type": "sidebar",
        "device": "desktop",
        "app": "hrms",
        "items": [
            {"action_type": "page", "target": "hrms.exec_dashboard", "icon": "activity", "route": "/hrms/executive/dashboard", "label": "Executive Dashboard"},
            {"action_type": "page", "target": "hrms.exec_workforce", "icon": "users", "route": "/hrms/executive/workforce", "label": "Workforce Overview"},
            {"action_type": "page", "target": "hrms.exec_payroll", "icon": "dollar-sign", "route": "/hrms/executive/payroll", "label": "Payroll Summary"},
            {"action_type": "page", "target": "hrms.exec_reports", "icon": "bar-chart-2", "route": "/hrms/executive/reports", "label": "Strategic Reports"},
        ],
    },

]