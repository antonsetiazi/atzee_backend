# verticals/agri/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — OWNER
    # ========================================
    {
        "tenant_code": None,
        "role": "Owner",
        "type": "sidebar",
        "device": "desktop",
        "app": "agri",
        "items": [
            {"action_type": "page", "target": "agri.owner.dashboard", "icon": "home", "route": "/agri/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "agri.farms", "icon": "map", "route": "/agri/farms", "label": "Farms"},
            {"action_type": "page", "target": "agri.cycles", "icon": "refresh-cw", "route": "/agri/cycles", "label": "Planting Cycles"},
            {"action_type": "page", "target": "agri.inventory", "icon": "package", "route": "/agri/inventory", "label": "Inventory"},
            {"action_type": "page", "target": "agri.finance", "icon": "dollar-sign", "route": "/agri/finance", "label": "Finance"},
            {"action_type": "page", "target": "agri.reports", "icon": "bar-chart-3", "route": "/agri/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — FARM MANAGER
    # ========================================
    {
        "tenant_code": None,
        "role": "Farm Manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "agri",
        "items": [
            {"action_type": "page", "target": "agri.manager.dashboard", "icon": "home", "route": "/agri/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "agri.farms", "icon": "map", "route": "/agri/farms", "label": "Farms"},
            {"action_type": "page", "target": "agri.cycles", "icon": "refresh-cw", "route": "/agri/cycles", "label": "Planting Cycles"},
            {"action_type": "page", "target": "agri.operations", "icon": "clipboard", "route": "/agri/operations", "label": "Operations"},
            {"action_type": "page", "target": "agri.resources", "icon": "users", "route": "/agri/resources", "label": "Resources"},
            {"action_type": "page", "target": "agri.inventory", "icon": "package", "route": "/agri/inventory", "label": "Inventory"},
            {"action_type": "page", "target": "agri.reports", "icon": "bar-chart-3", "route": "/agri/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — FIELD SUPERVISOR
    # ========================================
    {
        "tenant_code": None,
        "role": "Field Supervisor",
        "type": "sidebar",
        "device": "desktop",
        "app": "agri",
        "items": [
            {"action_type": "page", "target": "agri.supervisor.dashboard", "icon": "home", "route": "/agri/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "agri.cycles", "icon": "refresh-cw", "route": "/agri/cycles", "label": "Active Cycles"},
            {"action_type": "page", "target": "agri.operations", "icon": "clipboard", "route": "/agri/operations", "label": "Field Operations"},
            {"action_type": "page", "target": "agri.worklogs", "icon": "file-text", "route": "/agri/worklogs", "label": "Work Logs"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — WORKER
    # ========================================
    {
        "tenant_code": None,
        "role": "Worker",
        "type": "sidebar",
        "device": "desktop",
        "app": "agri",
        "items": [
            {"action_type": "page", "target": "agri.worker.dashboard", "icon": "home", "route": "/agri/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "agri.my_tasks", "icon": "check-square", "route": "/agri/tasks", "label": "My Tasks"},
            {"action_type": "page", "target": "agri.worklog.create", "icon": "edit", "route": "/agri/worklog/create", "label": "Input Work Log"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — FINANCE
    # ========================================
    {
        "tenant_code": None,
        "role": "Finance",
        "type": "sidebar",
        "device": "desktop",
        "app": "agri",
        "items": [
            {"action_type": "page", "target": "agri.finance.dashboard", "icon": "home", "route": "/agri/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "agri.cycles", "icon": "refresh-cw", "route": "/agri/cycles", "label": "Planting Cycles"},
            {"action_type": "page", "target": "agri.inventory", "icon": "package", "route": "/agri/inventory", "label": "Inventory Value"},
            {"action_type": "page", "target": "agri.finance", "icon": "dollar-sign", "route": "/agri/finance", "label": "Finance"},
            {"action_type": "page", "target": "agri.reports", "icon": "bar-chart-3", "route": "/agri/reports", "label": "Financial Reports"},
        ],
    },
]