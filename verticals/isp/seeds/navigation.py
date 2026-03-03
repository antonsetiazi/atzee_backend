# verticals/isp/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — OWNER (100)
    # ========================================
    {
        "tenant_code": None,
        "role": "owner",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.dashboard", "icon": "activity", "route": "/isp/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "isp.customers", "icon": "users", "route": "/isp/customers", "label": "Customers"},
            {"action_type": "page", "target": "isp.subscriptions", "icon": "wifi", "route": "/isp/subscriptions", "label": "Subscriptions"},
            {"action_type": "page", "target": "isp.invoices", "icon": "file-text", "route": "/isp/invoices", "label": "Invoices"},
            {"action_type": "page", "target": "isp.devices", "icon": "server", "route": "/isp/devices", "label": "Network Devices"},
            {"action_type": "page", "target": "isp.tickets", "icon": "alert-circle", "route": "/isp/tickets", "label": "Trouble Tickets"},
            {"action_type": "page", "target": "isp.reports", "icon": "bar-chart", "route": "/isp/reports", "label": "Reports"},
            {"action_type": "page", "target": "core.users", "icon": "shield", "route": "/core/users", "label": "Users & Roles"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — GENERAL MANAGER (90)
    # ========================================
    {
        "tenant_code": None,
        "role": "general manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.dashboard", "icon": "activity", "route": "/isp/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "isp.customers", "icon": "users", "route": "/isp/customers", "label": "Customers"},
            {"action_type": "page", "target": "isp.subscriptions", "icon": "wifi", "route": "/isp/subscriptions", "label": "Subscriptions"},
            {"action_type": "page", "target": "isp.invoices", "icon": "file-text", "route": "/isp/invoices", "label": "Invoices"},
            {"action_type": "page", "target": "isp.monitoring", "icon": "cpu", "route": "/isp/monitoring", "label": "Network Monitoring"},
            {"action_type": "page", "target": "isp.reports", "icon": "bar-chart", "route": "/isp/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — FINANCE MANAGER (80)
    # ========================================
    {
        "tenant_code": None,
        "role": "finance manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.dashboard", "icon": "activity", "route": "/isp/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "isp.invoices", "icon": "file-text", "route": "/isp/invoices", "label": "Invoices"},
            {"action_type": "page", "target": "isp.payments", "icon": "credit-card", "route": "/isp/payments", "label": "Payments"},
            {"action_type": "page", "target": "isp.financial_reports", "icon": "bar-chart-2", "route": "/isp/reports/finance", "label": "Financial Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — NETWORK ENGINEER (70)
    # ========================================
    {
        "tenant_code": None,
        "role": "network engineer",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.dashboard", "icon": "activity", "route": "/isp/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "isp.devices", "icon": "server", "route": "/isp/devices", "label": "Devices"},
            {"action_type": "page", "target": "isp.ip_pools", "icon": "layers", "route": "/isp/ip-pools", "label": "IP Pools"},
            {"action_type": "page", "target": "isp.bandwidth_profiles", "icon": "wifi", "route": "/isp/bandwidth", "label": "Bandwidth Profiles"},
            {"action_type": "page", "target": "isp.monitoring", "icon": "cpu", "route": "/isp/monitoring", "label": "Monitoring"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — NOC STAFF (60)
    # ========================================
    {
        "tenant_code": None,
        "role": "noc staff",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.dashboard", "icon": "activity", "route": "/isp/dashboard", "label": "Live Dashboard"},
            {"action_type": "page", "target": "isp.monitoring", "icon": "cpu", "route": "/isp/monitoring", "label": "Monitoring"},
            {"action_type": "page", "target": "isp.active_sessions", "icon": "wifi", "route": "/isp/sessions", "label": "Active Sessions"},
            {"action_type": "page", "target": "isp.tickets", "icon": "alert-circle", "route": "/isp/tickets", "label": "Trouble Tickets"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — BILLING STAFF (50)
    # ========================================
    {
        "tenant_code": None,
        "role": "billing staff",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.dashboard", "icon": "activity", "route": "/isp/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "isp.invoices", "icon": "file-text", "route": "/isp/invoices", "label": "Invoices"},
            {"action_type": "page", "target": "isp.payments", "icon": "credit-card", "route": "/isp/payments", "label": "Payments"},
            {"action_type": "page", "target": "isp.overdue", "icon": "alert-triangle", "route": "/isp/overdue", "label": "Overdue Accounts"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — CUSTOMER SERVICE (40)
    # ========================================
    {
        "tenant_code": None,
        "role": "customer service",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.dashboard", "icon": "activity", "route": "/isp/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "isp.customers", "icon": "users", "route": "/isp/customers", "label": "Customers"},
            {"action_type": "page", "target": "isp.tickets", "icon": "alert-circle", "route": "/isp/tickets", "label": "Trouble Tickets"},
            {"action_type": "page", "target": "isp.installations", "icon": "tool", "route": "/isp/installations", "label": "Installations"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — SALES MARKETING (30)
    # ========================================
    {
        "tenant_code": None,
        "role": "sales marketing",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.dashboard", "icon": "activity", "route": "/isp/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "isp.leads", "icon": "user-plus", "route": "/isp/leads", "label": "Leads"},
            {"action_type": "page", "target": "isp.sales_orders", "icon": "shopping-cart", "route": "/isp/sales", "label": "Sales Orders"},
            {"action_type": "page", "target": "isp.commissions", "icon": "trending-up", "route": "/isp/commissions", "label": "Commissions"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — FIELD TECHNICIAN (20)
    # ========================================
    {
        "tenant_code": None,
        "role": "field technician",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.my_tasks", "icon": "tool", "route": "/isp/tasks", "label": "My Tasks"},
            {"action_type": "page", "target": "isp.installations", "icon": "wifi", "route": "/isp/installations", "label": "Installations"},
            {"action_type": "page", "target": "isp.tickets", "icon": "alert-circle", "route": "/isp/tickets", "label": "Assigned Tickets"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — CUSTOMER (10)
    # ========================================
    {
        "tenant_code": None,
        "role": "customer",
        "type": "sidebar",
        "device": "desktop",
        "app": "isp",
        "items": [
            {"action_type": "page", "target": "isp.portal_dashboard", "icon": "home", "route": "/portal/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "isp.my_subscription", "icon": "wifi", "route": "/portal/subscription", "label": "My Subscription"},
            {"action_type": "page", "target": "isp.my_invoices", "icon": "file-text", "route": "/portal/invoices", "label": "My Invoices"},
            {"action_type": "page", "target": "isp.support", "icon": "message-circle", "route": "/portal/support", "label": "Support"},
        ],
    },

]