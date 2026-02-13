# core/ui/seed_pages.py

UI_PAGES = [
    # =====================
    # DASHBOARD
    # =====================
    {
        "key": "dashboard",
        "domain": "core",
        "entity": "dashboard",
        "title": "Dashboard",
        "permissions": ["core.dashboard.view"],
        "path": "/dashboard",
        "blocks": [
            {
                "type": "custom",
                "component": "DashboardOverview"
            }
        ],
    },

    # =====================
    # USERS
    # =====================
    {
        "key": "users.list",
        "domain": "core",
        "entity": "users",
        "title": "Users",
        "path": "/users",
        "permissions": ["core.users.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/core/users/",
                "columns": [
                    {"key": "username", "label": "Username"},
                    {"key": "email", "label": "Email"},
                    {"key": "is_active", "label": "Active"},
                ],
            }
        ],
    },

    # =====================
    # ROLES
    # =====================
    {
        "key": "roles.list",
        "domain": "core",
        "entity": "roles",
        "title": "Roles",
        "path": "/roles",
        "permissions": ["core.roles.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/core/roles/",
                "columns": [
                    {"key": "name", "label": "Role Name"},
                    {"key": "description", "label": "Description"},
                ],
            }
        ],
    },

    # =====================
    # PERMISSIONS
    # =====================
    {
        "key": "permissions.list",
        "domain": "core",
        "entity": "permissions",
        "title": "Permissions",
        "permissions": ["core.permissions.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/core/permissions/",
                "columns": [
                    {"key": "code", "label": "Code"},
                    {"key": "description", "label": "Description"},
                ],
            }
        ],
    },

    # =====================
    # TENANTS
    # =====================
    {
        "key": "tenants.list",
        "domain": "core",
        "entity": "tenants",
        "title": "Tenants",
        "path": "/tenants",
        "permissions": ["core.tenants.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/core/tenants/",
                "columns": [
                    {"key": "name", "label": "Tenant Name"},
                    {"key": "domain", "label": "Domain"},
                    {"key": "is_active", "label": "Active"},
                ],
            }
        ],
    },

    # =====================
    # AUDIT LOGS
    # =====================
    {
        "key": "audit_logs.list",
        "domain": "core",
        "entity": "audit_logs",
        "title": "Audit Logs",
        "path": "/audit-logs",
        "permissions": ["core.audit_logs.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/core/audit-logs/",
                "columns": [
                    {"key": "actor", "label": "User"},
                    {"key": "action", "label": "Action"},
                    {"key": "created_at", "label": "Time"},
                ],
            }
        ],
    },
]
