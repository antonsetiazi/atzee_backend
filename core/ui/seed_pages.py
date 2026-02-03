# core/ui/seed_pages.py

UI_PAGES = [
    # =====================
    # USERS
    # =====================
    {
        "key": "users.list",
        "domain": "core",
        "entity": "users",
        "title": "Users",
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
