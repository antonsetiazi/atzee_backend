# verticals/finance/seeds/navigation.py

NAVIGATION_SEED = [

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
        "app": "finance",
        "items": [
            {"action_type": "page", "target": "profile", "icon": "profile", "route": "/account/profile", "label": "Profil"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
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
        "app": "finance",
        "items": [
            {"action_type": "page", "target": "dashboard", "icon": "home", "route": "/dashboard", "label": "Home"},
            {"action_type": "page", "target": "help", "icon": "help", "route": "/business/help", "label": "Help"},
        ],
    },

    # =========================
    # Guest
    # =========================
    # Desktop Sidebar
    # =========================
    {
        "tenant_code": None,
        "role": "guest",
        "type": "sidebar",
        "device": "desktop",
        "app": "finance",
        "items": [
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "partner", "icon": "search", "route": "/services", "label": "Cari Ustadz"},
        ],
    },

    
    # =========================
    # Mobile Bottom
    # =========================
    {
        "tenant_code": None,
        "role": "guest",
        "type": "bottom",
        "device": "mobile",
        "app": "finance",
        "items": [
            {"action_type": "page", "target": "login", "icon": "login", "route": "/login", "label": "Login"},
            {"action_type": "page", "target": "home", "icon": "home", "route": "/dashboard", "label": "Beranda"},
            {"action_type": "page", "target": "partner", "icon": "search", "route": "/services", "label": "Cari Ustadz"},            
        ],
    },
]
