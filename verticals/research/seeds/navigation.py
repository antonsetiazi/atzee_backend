# verticals/research/seeds/navigation.py

NAVIGATION_SEED = [

    # ========================================
    # DESKTOP SIDEBAR — ADMIN
    # ========================================
    {
        "tenant_code": None,
        "role": "Admin",
        "type": "sidebar",
        "device": "desktop",
        "app": "research",
        "items": [
            {"action_type": "page", "target": "research.admin.dashboard", "icon": "home", "route": "/research/dashboard/admin", "label": "Dashboard"},
            {"action_type": "page", "target": "research.governance.programs", "icon": "layers", "route": "/research/governance/programs", "label": "Governance"},
            {"action_type": "page", "target": "research.pipeline.proposals", "icon": "file-text", "route": "/research/pipeline/proposals", "label": "Research Pipeline"},
            {"action_type": "page", "target": "research.projects.list", "icon": "flask", "route": "/research/projects", "label": "Active Projects"},
            {"action_type": "page", "target": "research.archive", "icon": "archive", "route": "/research/archive", "label": "Archive"},
            {"action_type": "page", "target": "research.reports", "icon": "bar-chart-2", "route": "/research/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — RESEARCH DIRECTOR
    # ========================================
    {
        "tenant_code": None,
        "role": "Research Director",
        "type": "sidebar",
        "device": "desktop",
        "app": "research",
        "items": [
            {"action_type": "page", "target": "research.director.dashboard", "icon": "home", "route": "/research/dashboard/director", "label": "Dashboard"},
            {"action_type": "page", "target": "research.governance.programs", "icon": "layers", "route": "/research/governance/programs", "label": "Governance"},
            {"action_type": "page", "target": "research.pipeline.proposals", "icon": "file-text", "route": "/research/pipeline/proposals", "label": "Research Pipeline"},
            {"action_type": "page", "target": "research.projects.list", "icon": "flask", "route": "/research/projects", "label": "Active Projects"},
            {"action_type": "page", "target": "research.funding.overview", "icon": "dollar-sign", "route": "/research/funding", "label": "Funding & Budget"},
            {"action_type": "page", "target": "research.publications", "icon": "book-open", "route": "/research/publications", "label": "Publications"},
            {"action_type": "page", "target": "research.reports", "icon": "bar-chart-2", "route": "/research/reports", "label": "Reports"},
            {"action_type": "page", "target": "research.archive", "icon": "archive", "route": "/research/archive", "label": "Archive"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — COMMITTEE MEMBER
    # ========================================
    {
        "tenant_code": None,
        "role": "Committee Member",
        "type": "sidebar",
        "device": "desktop",
        "app": "research",
        "items": [
            {"action_type": "page", "target": "research.committee.dashboard", "icon": "home", "route": "/research/dashboard/committee", "label": "Dashboard"},
            {"action_type": "page", "target": "research.governance.programs", "icon": "layers", "route": "/research/governance/programs", "label": "Governance"},
            {"action_type": "page", "target": "research.pipeline.proposals", "icon": "file-check", "route": "/research/pipeline/proposals", "label": "Proposals"},
            {"action_type": "page", "target": "research.funding.overview", "icon": "dollar-sign", "route": "/research/funding", "label": "Funding & Budget"},
            {"action_type": "page", "target": "research.reports", "icon": "bar-chart-2", "route": "/research/reports", "label": "Reports"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — REVIEWER
    # ========================================
    {
        "tenant_code": None,
        "role": "Reviewer",
        "type": "sidebar",
        "device": "desktop",
        "app": "research",
        "items": [
            {"action_type": "page", "target": "research.reviewer.dashboard", "icon": "home", "route": "/research/dashboard/reviewer", "label": "Dashboard"},
            {"action_type": "page", "target": "research.pipeline.assigned", "icon": "file-text", "route": "/research/pipeline/assigned", "label": "Assigned Proposals"},
            {"action_type": "page", "target": "research.archive", "icon": "archive", "route": "/research/archive", "label": "Review History"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — PRINCIPAL INVESTIGATOR
    # ========================================
    {
        "tenant_code": None,
        "role": "Principal Investigator",
        "type": "sidebar",
        "device": "desktop",
        "app": "research",
        "items": [
            {"action_type": "page", "target": "research.pi.dashboard", "icon": "home", "route": "/research/dashboard/pi", "label": "Dashboard"},
            {"action_type": "page", "target": "research.pipeline.my_proposals", "icon": "file-text", "route": "/research/pipeline/my", "label": "My Proposals"},
            {"action_type": "page", "target": "research.projects.my", "icon": "flask", "route": "/research/projects/my", "label": "My Projects"},
            {"action_type": "page", "target": "research.funding.project_budget", "icon": "dollar-sign", "route": "/research/funding/project", "label": "Project Budget"},
            {"action_type": "page", "target": "research.publications.my", "icon": "book-open", "route": "/research/publications/my", "label": "Publications"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — RESEARCHER
    # ========================================
    {
        "tenant_code": None,
        "role": "Researcher",
        "type": "sidebar",
        "device": "desktop",
        "app": "research",
        "items": [
            {"action_type": "page", "target": "research.researcher.dashboard", "icon": "home", "route": "/research/dashboard/researcher", "label": "Dashboard"},
            {"action_type": "page", "target": "research.projects.assigned", "icon": "flask", "route": "/research/projects/assigned", "label": "Assigned Projects"},
            {"action_type": "page", "target": "research.publications.contribute", "icon": "book-open", "route": "/research/publications/contribute", "label": "Publications"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — RESEARCH ASSISTANT
    # ========================================
    {
        "tenant_code": None,
        "role": "Research Assistant",
        "type": "sidebar",
        "device": "desktop",
        "app": "research",
        "items": [
            {"action_type": "page", "target": "research.assistant.dashboard", "icon": "home", "route": "/research/dashboard/assistant", "label": "Dashboard"},
            {"action_type": "page", "target": "research.projects.support", "icon": "flask", "route": "/research/projects/support", "label": "Supporting Projects"},
            {"action_type": "page", "target": "research.archive", "icon": "archive", "route": "/research/archive", "label": "Archive"},
        ],
    },

    # ========================================
    # DESKTOP SIDEBAR — FINANCE OFFICER
    # ========================================
    {
        "tenant_code": None,
        "role": "Finance Officer",
        "type": "sidebar",
        "device": "desktop",
        "app": "research",
        "items": [
            {"action_type": "page", "target": "research.finance.dashboard", "icon": "home", "route": "/research/dashboard/finance", "label": "Dashboard"},
            {"action_type": "page", "target": "research.funding.sources", "icon": "dollar-sign", "route": "/research/funding/sources", "label": "Funding Sources"},
            {"action_type": "page", "target": "research.funding.grants", "icon": "file-text", "route": "/research/funding/grants", "label": "Grants"},
            {"action_type": "page", "target": "research.reports.budget", "icon": "bar-chart-2", "route": "/research/reports/budget", "label": "Budget Report"},
        ],
    },
]