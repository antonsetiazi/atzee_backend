# verticals/koperasi/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — KETUA
    # ========================================
    {
        "tenant_code": None,
        "role": "Ketua",
        "type": "sidebar",
        "device": "desktop",
        "app": "koperasi",
        "items": [
            {"action_type": "page", "target": "koperasi.dashboard", "icon": "home", "route": "/koperasi/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "koperasi.members", "icon": "users", "route": "/koperasi/members", "label": "Members"},
            {"action_type": "page", "target": "koperasi.savings", "icon": "wallet", "route": "/koperasi/savings", "label": "Savings"},
            {"action_type": "page", "target": "koperasi.loans", "icon": "credit-card", "route": "/koperasi/loans", "label": "Loans"},
            {"action_type": "page", "target": "koperasi.shu", "icon": "trending-up", "route": "/koperasi/shu", "label": "SHU"},
            {"action_type": "page", "target": "koperasi.rat", "icon": "calendar", "route": "/koperasi/rat", "label": "RAT"},
            {"action_type": "page", "target": "koperasi.reports", "icon": "bar-chart", "route": "/koperasi/reports", "label": "Reports"},
            {"action_type": "page", "target": "koperasi.settings", "icon": "settings", "route": "/koperasi/settings", "label": "Settings"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — BENDAHARA
    # ========================================
    {
        "tenant_code": None,
        "role": "Bendahara",
        "type": "sidebar",
        "device": "desktop",
        "app": "koperasi",
        "items": [
            {"action_type": "page", "target": "koperasi.dashboard_finance", "icon": "home", "route": "/koperasi/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "koperasi.members", "icon": "users", "route": "/koperasi/members", "label": "Members"},
            {"action_type": "page", "target": "koperasi.savings", "icon": "wallet", "route": "/koperasi/savings", "label": "Savings"},
            {"action_type": "page", "target": "koperasi.loans", "icon": "credit-card", "route": "/koperasi/loans", "label": "Loans"},
            {"action_type": "page", "target": "koperasi.shu_draft", "icon": "trending-up", "route": "/koperasi/shu", "label": "SHU"},
            {"action_type": "page", "target": "koperasi.reports_finance", "icon": "bar-chart", "route": "/koperasi/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — PENGAWAS
    # ========================================
    {
        "tenant_code": None,
        "role": "Pengawas",
        "type": "sidebar",
        "device": "desktop",
        "app": "koperasi",
        "items": [
            {"action_type": "page", "target": "koperasi.dashboard_audit", "icon": "activity", "route": "/koperasi/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "koperasi.members_read", "icon": "users", "route": "/koperasi/members", "label": "Members"},
            {"action_type": "page", "target": "koperasi.savings_read", "icon": "wallet", "route": "/koperasi/savings", "label": "Savings"},
            {"action_type": "page", "target": "koperasi.loans_read", "icon": "credit-card", "route": "/koperasi/loans", "label": "Loans"},
            {"action_type": "page", "target": "koperasi.shu_read", "icon": "trending-up", "route": "/koperasi/shu", "label": "SHU"},
            {"action_type": "page", "target": "koperasi.audit_logs", "icon": "file-text", "route": "/koperasi/audit", "label": "Audit Logs"},
            {"action_type": "page", "target": "koperasi.reports", "icon": "bar-chart", "route": "/koperasi/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — STAFF
    # ========================================
    {
        "tenant_code": None,
        "role": "Staff",
        "type": "sidebar",
        "device": "desktop",
        "app": "koperasi",
        "items": [
            {"action_type": "page", "target": "koperasi.dashboard", "icon": "home", "route": "/koperasi/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "koperasi.members_create", "icon": "user-plus", "route": "/koperasi/members", "label": "Members"},
            {"action_type": "page", "target": "koperasi.savings_input", "icon": "wallet", "route": "/koperasi/savings", "label": "Savings"},
            {"action_type": "page", "target": "koperasi.loans_input", "icon": "credit-card", "route": "/koperasi/loans", "label": "Loans"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — MEMBER
    # ========================================
    {
        "tenant_code": None,
        "role": "Member",
        "type": "sidebar",
        "device": "desktop",
        "app": "koperasi",
        "items": [
            {"action_type": "page", "target": "koperasi.my_dashboard", "icon": "home", "route": "/koperasi/my/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "koperasi.my_savings", "icon": "wallet", "route": "/koperasi/my/savings", "label": "My Savings"},
            {"action_type": "page", "target": "koperasi.my_loans", "icon": "credit-card", "route": "/koperasi/my/loans", "label": "My Loans"},
            {"action_type": "page", "target": "koperasi.my_shu", "icon": "trending-up", "route": "/koperasi/my/shu", "label": "My SHU"},
            {"action_type": "page", "target": "koperasi.my_statements", "icon": "file-text", "route": "/koperasi/my/statements", "label": "Statements"},
        ],
    },

]