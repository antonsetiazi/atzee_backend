# core/ui/seed_menus.py

UI_MENUS = [
    # =====================
    # DASHBOARD
    # =====================
    {
        "key": "dashboard",
        "label": "Dashboard",
        "icon": "layout-dashboard",
        "parent": None,
        "app": "core",
        "resource": "dashboard",
        "action": "view",
        "route": "/dashboard",
        "order": 1,
    },

    # =====================
    # USER MANAGEMENT
    # =====================
    {
        "key": "users",
        "label": "Users & Access",
        "icon": "users",
        "parent": None,
        "app": "core",
        "resource": "users",
        "action": "view",
        "route": "/users",
        "order": 10,
    },
    {
        "key": "users.list",
        "label": "Users",
        "parent": "users",
        "app": "core",
        "resource": "users",
        "action": "view",
        "route": "/users",
        "order": 1,
    },
    {
        "key": "roles.list",
        "label": "Roles",
        "parent": "users",
        "app": "core",
        "resource": "roles",
        "action": "view",
        "route": "/roles",
        "order": 2,
    },
    {
        "key": "permissions.list",
        "label": "Permissions",
        "parent": "users",
        "app": "core",
        "resource": "permissions",
        "action": "view",
        "route": "/permissions",
        "order": 3,
    },

    # =====================
    # TENANT
    # =====================
    {
        "key": "tenants.list",
        "label": "Tenants",
        "icon": "building",
        "parent": None,
        "app": "core",
        "resource": "tenants",
        "action": "view",
        "route": "/tenants",
        "order": 20,
    },

    # =====================
    # SYSTEM
    # =====================
    {
        "key": "system",
        "label": "System",
        "icon": "settings",
        "parent": None,
        "app": "core",
        "resource": "settings",
        "action": "view",
        "route": "/system",
        "order": 30,
    },
    {
        "key": "audit_logs.list",
        "label": "Audit Logs",
        "parent": "system",
        "app": "core",
        "resource": "audit_logs",
        "action": "view",
        "route": "/audit-logs",
        "order": 1,
    },
    {
        "key": "settings.general",
        "label": "Settings",
        "parent": "system",
        "app": "core",
        "resource": "settings",
        "action": "view",
        "route": "/settings",
        "order": 2,
    },
]