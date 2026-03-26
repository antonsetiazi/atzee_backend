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
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "partner", "icon": "search", "route": "/services", "label": "Cari Ustadz"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "transactions", "icon": "transaction", "route": "/business/transaction", "label": "Transaksi"},
            {"action_type": "page", "target": "booking", "icon": "booking", "route": "/business/my-bookings", "label": "Booking"},
        ],
    },

    # =========================
    # Desktop Sidebar - Customer
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
            {"action_type": "page", "target": "transactions", "icon": "transaction", "route": "/business/transaction", "label": "Transaksi"},
            {"action_type": "page", "target": "booking", "icon": "booking", "route": "/business/my-bookings", "label": "Booking"},
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

    # =========================
    # Mobile Bottom - Guest
    # =========================
    {
        "tenant_code": None,
        "role": "guest",
        "type": "bottom",
        "device": "mobile",
        "app": "ustadzku",
        "items": [
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "partner", "icon": "search", "route": "/services", "label": "Cari Ustadz"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "transactions", "icon": "transaction", "route": "/business/transaction", "label": "Transaksi"},
            {"action_type": "page", "target": "booking", "icon": "booking", "route": "/business/my-bookings", "label": "Booking"},
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
            {"action_type": "page", "target": "transactions", "icon": "transaction", "route": "/business/transaction", "label": "Transaksi"},
            {"action_type": "page", "target": "booking", "icon": "booking", "route": "/business/my-bookings", "label": "Booking"},
        ],
    },
]
