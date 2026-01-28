# hr/ui/seed_menus.py

UI_MENUS = [
    # =====================
    # EMPLOYEES
    # =====================
    {
        "key": "employees.list",
        "label": "Employees",
        "icon": "user",
        "parent": None,
        "app": "hr",
        "resource": "employees",
        "action": "view",
        "route": "/hr/employees",
        "order": 10,
    },

    # =====================
    # ATTENDANCE
    # =====================
    {
        "key": "attendance.list",
        "label": "Attendance",
        "icon": "clock",
        "parent": None,
        "app": "hr",
        "resource": "attendance",
        "action": "view",
        "route": "/hr/attendance",
        "order": 20,
    },

    # =====================
    # PAYROLL
    # =====================
    {
        "key": "payroll.list",
        "label": "Payroll",
        "icon": "credit-card",
        "parent": None,
        "app": "hr",
        "resource": "payroll",
        "action": "view",
        "route": "/hr/payroll",
        "order": 30,
    },

    # =====================
    # ASSETS
    # =====================
    {
        "key": "assets.list",
        "label": "Assets",
        "icon": "archive",
        "parent": None,
        "app": "hr",
        "resource": "assets",
        "action": "view",
        "route": "/hr/assets",
        "order": 40,
    },
]
