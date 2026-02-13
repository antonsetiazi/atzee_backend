# core/ui/seed_navigations.py

from typing import List, Dict

"""
Navigation Strategy Seed
Now fully strategy-based (not menu-only).
"""

NAVIGATION_SEED: List[Dict] = [
    # =========================
    # BUSINESS APP - MANAGER
    # =========================
    {
        "tenant_code": None,
        "role": "manager",
        "type": "bottom",
        "device": "mobile",
        "app": "business",
        "items": [
            {
                "action_type": "page",
                "target": "dashboard",
                "icon": "home",
            },
            {
                "action_type": "page",
                "target": "customers.list",
                "icon": "user-check",
            },
            {
                "action_type": "workflow",
                "target": "orders.create",
                "icon": "plus",
                "is_primary": True,
            },
        ],
    },

    # =========================
    # BUSINESS APP - STAFF
    # =========================
    {
        "tenant_code": None,
        "role": "staff",
        "type": "bottom",
        "device": "mobile",
        "app": "business",
        "items": [
            {
                "action_type": "page",
                "target": "dashboard.main",
                "icon": "home",
            },
            {
                "action_type": "entity",
                "target": "customers.list",
                "icon": "user-check",
            },
        ],
    },

    # =========================
    # DESKTOP SIDEBAR - MANAGER
    # =========================
    {
        "tenant_code": None,
        "role": "manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "business",
        "items": [
            {
                "action_type": "menu",
                "target": "dashboard.main",
            },
            {
                "action_type": "menu",
                "target": "customers.list",
            },
            {
                "action_type": "menu",
                "target": "orders.list",
            },
            {
                "action_type": "menu",
                "target": "settings.profile",
            },
        ],
    },
]
