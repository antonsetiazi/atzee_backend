# verticals/bengkel/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — OWNER
    # ========================================
    {
        "tenant_code": None,
        "role": "owner",
        "type": "sidebar",
        "device": "desktop",
        "app": "bengkel",
        "items": [
            {"action_type": "page", "target": "bengkel.dashboard", "icon": "home", "route": "/bengkel/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "bengkel.work_orders", "icon": "clipboard", "route": "/bengkel/work-orders", "label": "Work Orders"},
            {"action_type": "page", "target": "bengkel.vehicles", "icon": "truck", "route": "/bengkel/vehicles", "label": "Vehicles"},
            {"action_type": "page", "target": "bengkel.customers", "icon": "users", "route": "/business/partners", "label": "Customers"},
            {"action_type": "page", "target": "bengkel.services", "icon": "tool", "route": "/bengkel/services", "label": "Services"},
            {"action_type": "page", "target": "inventory.snapshot", "icon": "box", "route": "/business/inventory", "label": "Spareparts"},
            {"action_type": "page", "target": "bengkel.mechanics", "icon": "user-check", "route": "/bengkel/mechanics", "label": "Mechanics"},
            {"action_type": "page", "target": "bengkel.appointments", "icon": "calendar", "route": "/bengkel/appointments", "label": "Appointments"},
            {"action_type": "page", "target": "bengkel.finance", "icon": "credit-card", "route": "/business/transactions", "label": "Finance"},
            {"action_type": "page", "target": "bengkel.reports", "icon": "bar-chart", "route": "/bengkel/reports", "label": "Reports"},
            {"action_type": "page", "target": "bengkel.settings", "icon": "settings", "route": "/bengkel/settings", "label": "Settings"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — SERVICE ADVISOR
    # ========================================
    {
        "tenant_code": None,
        "role": "service advisor",
        "type": "sidebar",
        "device": "desktop",
        "app": "bengkel",
        "items": [
            {"action_type": "page", "target": "bengkel.dashboard", "icon": "home", "route": "/bengkel/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "bengkel.work_orders", "icon": "clipboard", "route": "/bengkel/work-orders", "label": "Work Orders"},
            {"action_type": "page", "target": "bengkel.vehicles", "icon": "truck", "route": "/bengkel/vehicles", "label": "Vehicles"},
            {"action_type": "page", "target": "bengkel.customers", "icon": "users", "route": "/business/partners", "label": "Customers"},
            {"action_type": "page", "target": "bengkel.appointments", "icon": "calendar", "route": "/bengkel/appointments", "label": "Appointments"},
            {"action_type": "page", "target": "inventory.snapshot", "icon": "box", "route": "/business/inventory", "label": "Spareparts"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — MECHANIC
    # ========================================
    {
        "tenant_code": None,
        "role": "mechanic",
        "type": "sidebar",
        "device": "desktop",
        "app": "bengkel",
        "items": [
            {"action_type": "page", "target": "bengkel.my_jobs", "icon": "tool", "route": "/bengkel/my-jobs", "label": "My Jobs"},
            {"action_type": "page", "target": "bengkel.checklist", "icon": "check-square", "route": "/bengkel/checklist", "label": "Checklist"},
            {"action_type": "page", "target": "bengkel.parts_request", "icon": "package", "route": "/bengkel/parts-request", "label": "Parts Request"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — CASHIER
    # ========================================
    {
        "tenant_code": None,
        "role": "cashier",
        "type": "sidebar",
        "device": "desktop",
        "app": "bengkel",
        "items": [
            {"action_type": "page", "target": "bengkel.work_orders_done", "icon": "clipboard", "route": "/bengkel/work-orders?status=done", "label": "Completed Jobs"},
            {"action_type": "page", "target": "bengkel.invoice", "icon": "file-text", "route": "/business/transactions", "label": "Invoices"},
            {"action_type": "page", "target": "bengkel.payment", "icon": "credit-card", "route": "/business/payments", "label": "Payments"},
            {"action_type": "page", "target": "bengkel.closing", "icon": "dollar-sign", "route": "/bengkel/closing", "label": "Daily Closing"},
        ],
    },

]