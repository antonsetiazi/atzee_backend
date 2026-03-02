# verticals/ustadzku/seeds/navigation.py

NAVIGATION_SEED = [
    # =========================
    # Mobile Bottom - Customer
    # =========================
    {
        "tenant_code": None,        # semua tenant ustadzku
        "role": "customer",
        "type": "bottom",
        "device": "mobile",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "dashboard", "icon": "home", "route": "/dashboard", "label": "Home"},
            {"action_type": "page", "target": "booking", "icon": "booking", "route": "/business/my-bookings", "label": "Booking"},
            # {"action_type": "page", "target": "products.list", "icon": "box"},
        ],
    },

    # =========================
    # Mobile Bottom - Partner
    # =========================
    {
        "tenant_code": None,
        "role": "partner",
        "type": "bottom",
        "device": "mobile",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "dashboard", "icon": "home", "route": "/dashboard", "label": "Home"},
            {"action_type": "page", "target": "my_products.list", "icon": "box"},
            {"action_type": "page", "target": "sales.list", "icon": "dollar-sign"},
        ],
    },

    # =========================
    # Desktop Sidebar - Admin / Staff
    # =========================
    {
        "tenant_code": None,
        "role": "admin",
        "type": "sidebar",
        "device": "desktop",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "dashboard", "icon": "home", "route": "/dashboard", "label": "Home"},
            {"action_type": "page", "target": "notification", "icon": "notification", "route": "/core/notifications", "label": "Notification"},
            {"action_type": "page", "target": "booking", "icon": "booking", "route": "/business/my-bookings", "label": "Booking"},
            {"action_type": "page", "target": "help", "icon": "help", "route": "/business/help", "label": "Help"},
        ],
    },
]
