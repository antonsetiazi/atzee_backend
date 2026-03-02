# verticals/pos/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — CASHIER
    # ========================================
    {
        "tenant_code": None,
        "role": "cashier",
        "type": "sidebar",
        "device": "desktop",
        "app": "pos",
        "items": [
            {"action_type": "page", "target": "pos.dashboard", "icon": "home", "route": "/pos/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "pos.new_sale", "icon": "shopping-cart", "route": "/pos/sale", "label": "New Sale"},
            {"action_type": "page", "target": "pos.held", "icon": "pause-circle", "route": "/pos/held", "label": "Held"},
            {"action_type": "page", "target": "pos.refund", "icon": "rotate-ccw", "route": "/pos/refund", "label": "Refund"},
            {"action_type": "page", "target": "pos.shift", "icon": "clock", "route": "/pos/shift", "label": "Shift"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — SUPERVISOR
    # ========================================
    {
        "tenant_code": None,
        "role": "supervisor",
        "type": "sidebar",
        "device": "desktop",
        "app": "pos",
        "items": [
            {"action_type": "page", "target": "pos.dashboard", "icon": "home", "route": "/pos/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "pos.new_sale", "icon": "shopping-cart", "route": "/pos/sale", "label": "New Sale"},
            {"action_type": "page", "target": "pos.transactions", "icon": "file-text", "route": "/pos/transactions", "label": "Transactions"},
            {"action_type": "page", "target": "pos.shift_manage", "icon": "clock", "route": "/pos/shift", "label": "Shift Management"},
            {"action_type": "page", "target": "pos.reports", "icon": "bar-chart", "route": "/pos/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — MANAGER
    # ========================================
    {
        "tenant_code": None,
        "role": "manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "pos",
        "items": [
            {"action_type": "page", "target": "pos.dashboard", "icon": "home", "route": "/pos/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "pos.transactions", "icon": "file-text", "route": "/pos/transactions", "label": "Transactions"},
            {"action_type": "page", "target": "pos.reports", "icon": "bar-chart", "route": "/pos/reports", "label": "Reports"},
            {"action_type": "page", "target": "inventory.snapshot", "icon": "box", "route": "/business/inventory", "label": "Inventory"},
            {"action_type": "page", "target": "pos.staff", "icon": "users", "route": "/pos/staff", "label": "Staff"},
            {"action_type": "page", "target": "pos.settings", "icon": "settings", "route": "/pos/settings", "label": "Outlet Settings"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — AREA MANAGER
    # ========================================
    {
        "tenant_code": None,
        "role": "area manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "pos",
        "items": [
            {"action_type": "page", "target": "pos.global_dashboard", "icon": "activity", "route": "/pos/global", "label": "Global Dashboard"},
            {"action_type": "page", "target": "pos.outlet_performance", "icon": "trending-up", "route": "/pos/outlets", "label": "Outlet Performance"},
            {"action_type": "page", "target": "pos.reports", "icon": "bar-chart", "route": "/pos/reports", "label": "Reports"},
        ],
    },

]