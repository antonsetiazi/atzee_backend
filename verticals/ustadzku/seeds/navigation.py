# verticals/ustadzku/seeds/navigation.py

NAVIGATION_SEED = [

    # =========================
    # Customer
    # =========================
    # Mobile Bottom
    # =========================
    {
        "tenant_code": None,
        "role": "customer",
        "type": "bottom",
        "device": "mobile",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "partner", "icon": "search", "route": "/services", "label": "Cari Ustadz"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "orders", "icon": "order", "route": "/orders", "label": "Order"},
        ],
    },

    # =========================
    # Desktop Sidebar
    # =========================
    {
        "tenant_code": None,        # semua tenant ustadzku
        "role": "customer",
        "type": "sidebar",
        "device": "desktop",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "partner", "icon": "search", "route": "/services", "label": "Cari Ustadz"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "orders", "icon": "order", "route": "/orders", "label": "Order"},
        ],
    },


    # =========================
    # Partner
    # =========================
    # Mobile Bottom
    # =========================
    {
        "tenant_code": None,
        "role": "partner",
        "type": "bottom",
        "device": "mobile",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "orders", "icon": "order", "route": "/partner/orders", "label": "Order"},
        ],
    },

    # =========================
    # Desktop Sidebar
    # =========================
    {
        "tenant_code": None,
        "role": "partner",
        "type": "sidebar",
        "device": "desktop",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "orders", "icon": "order", "route": "/partner/orders", "label": "Order"},
        ],
    },


    # =========================
    # Admin / Staff
    # =========================
    # Mobile Bottom
    # =========================
    {
        "tenant_code": None,
        "role": "admin",
        "type": "bottom",
        "device": "mobile",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "orders", "icon": "order", "route": "/partner/orders", "label": "Order"},
        ],
    },

    # =========================
    # Desktop Sidebar
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

    # =========================
    # Desktop Sidebar - Guest
    # =========================
    {
        "tenant_code": None,
        "role": "guest",
        "type": "sidebar",
        "device": "desktop",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "partner", "icon": "search", "route": "/services", "label": "Cari Ustadz"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "booking", "icon": "booking", "route": "/business/my-bookings", "label": "Booking"},
        ],
    },
]
