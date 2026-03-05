# verticals/cbs/seeds/navigation.py

NAVIGATION_SEED = [

    # =====================================================
    # DESKTOP SIDEBAR — DIRECTOR
    # =====================================================
    {
        "tenant_code": None,
        "role": "Director",
        "type": "sidebar",
        "device": "desktop",
        "app": "cbs",
        "items": [
            {"action_type": "page", "target": "cbs.director.dashboard", "icon": "home", "route": "/cbs/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "cbs.customers", "icon": "users", "route": "/cbs/customers", "label": "Customers"},
            {"action_type": "page", "target": "cbs.accounts", "icon": "credit-card", "route": "/cbs/accounts", "label": "Accounts"},
            {"action_type": "page", "target": "cbs.loans", "icon": "file-text", "route": "/cbs/loans", "label": "Loans"},
            {"action_type": "page", "target": "cbs.treasury", "icon": "activity", "route": "/cbs/treasury", "label": "Treasury"},
            {"action_type": "page", "target": "cbs.compliance", "icon": "shield", "route": "/cbs/compliance", "label": "Compliance"},
            {"action_type": "page", "target": "cbs.reports", "icon": "bar-chart", "route": "/cbs/reports", "label": "Reports"},
            {"action_type": "page", "target": "cbs.administration", "icon": "settings", "route": "/cbs/admin", "label": "Administration"},
        ],
    },

    # =====================================================
    # DESKTOP SIDEBAR — BRANCH MANAGER
    # =====================================================
    {
        "tenant_code": None,
        "role": "Branch Manager",
        "type": "sidebar",
        "device": "desktop",
        "app": "cbs",
        "items": [
            {"action_type": "page", "target": "cbs.branch_manager.dashboard", "icon": "home", "route": "/cbs/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "cbs.branch.customers", "icon": "users", "route": "/cbs/customers", "label": "Customers"},
            {"action_type": "page", "target": "cbs.branch.accounts", "icon": "credit-card", "route": "/cbs/accounts", "label": "Accounts"},
            {"action_type": "page", "target": "cbs.branch.transactions", "icon": "repeat", "route": "/cbs/transactions", "label": "Transactions"},
            {"action_type": "page", "target": "cbs.branch.loans", "icon": "file-text", "route": "/cbs/loans", "label": "Loans"},
            {"action_type": "page", "target": "cbs.branch.reports", "icon": "bar-chart", "route": "/cbs/reports", "label": "Reports"},
        ],
    },

    # =====================================================
    # DESKTOP SIDEBAR — CREDIT OFFICER
    # =====================================================
    {
        "tenant_code": None,
        "role": "Credit Officer",
        "type": "sidebar",
        "device": "desktop",
        "app": "cbs",
        "items": [
            {"action_type": "page", "target": "cbs.credit_officer.dashboard", "icon": "home", "route": "/cbs/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "cbs.loan.pipeline", "icon": "git-branch", "route": "/cbs/loans/pipeline", "label": "Loan Pipeline"},
            {"action_type": "page", "target": "cbs.loan.applications", "icon": "file-plus", "route": "/cbs/loans/applications", "label": "Applications"},
            {"action_type": "page", "target": "cbs.loan.collateral", "icon": "shield", "route": "/cbs/loans/collateral", "label": "Collateral"},
            {"action_type": "page", "target": "cbs.loan.reports", "icon": "bar-chart", "route": "/cbs/reports/loans", "label": "Loan Reports"},
        ],
    },

    # =====================================================
    # DESKTOP SIDEBAR — TELLER
    # =====================================================
    {
        "tenant_code": None,
        "role": "Teller",
        "type": "sidebar",
        "device": "desktop",
        "app": "cbs",
        "items": [
            {"action_type": "page", "target": "cbs.teller.dashboard", "icon": "home", "route": "/cbs/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "cbs.transaction.deposit", "icon": "plus-circle", "route": "/cbs/transactions/deposit", "label": "Cash Deposit"},
            {"action_type": "page", "target": "cbs.transaction.withdrawal", "icon": "minus-circle", "route": "/cbs/transactions/withdrawal", "label": "Cash Withdrawal"},
            {"action_type": "page", "target": "cbs.transaction.transfer", "icon": "repeat", "route": "/cbs/transactions/transfer", "label": "Internal Transfer"},
            {"action_type": "page", "target": "cbs.closing", "icon": "clock", "route": "/cbs/closing", "label": "End of Day"},
        ],
    },

    # =====================================================
    # DESKTOP SIDEBAR — BACK OFFICE
    # =====================================================
    {
        "tenant_code": None,
        "role": "Back Office",
        "type": "sidebar",
        "device": "desktop",
        "app": "cbs",
        "items": [
            {"action_type": "page", "target": "cbs.back_office.dashboard", "icon": "home", "route": "/cbs/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "cbs.reversal", "icon": "rotate-ccw", "route": "/cbs/transactions/reversal", "label": "Reversal Approval"},
            {"action_type": "page", "target": "cbs.settlement", "icon": "shuffle", "route": "/cbs/treasury/settlement", "label": "Settlement"},
            {"action_type": "page", "target": "cbs.gl.reconciliation", "icon": "book", "route": "/cbs/treasury/reconciliation", "label": "GL Reconciliation"},
            {"action_type": "page", "target": "cbs.reports", "icon": "bar-chart", "route": "/cbs/reports", "label": "Reports"},
        ],
    },

    # =====================================================
    # DESKTOP SIDEBAR — COMPLIANCE OFFICER
    # =====================================================
    {
        "tenant_code": None,
        "role": "Compliance Officer",
        "type": "sidebar",
        "device": "desktop",
        "app": "cbs",
        "items": [
            {"action_type": "page", "target": "cbs.compliance.dashboard", "icon": "home", "route": "/cbs/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "cbs.aml.monitoring", "icon": "shield", "route": "/cbs/compliance/aml", "label": "AML Monitoring"},
            {"action_type": "page", "target": "cbs.str", "icon": "alert-circle", "route": "/cbs/compliance/str", "label": "STR Reports"},
            {"action_type": "page", "target": "cbs.ctr", "icon": "file-text", "route": "/cbs/compliance/ctr", "label": "CTR Reports"},
            {"action_type": "page", "target": "cbs.audit.logs", "icon": "activity", "route": "/cbs/compliance/audit", "label": "Audit Logs"},
        ],
    },

    # =====================================================
    # DESKTOP SIDEBAR — AUDITOR
    # =====================================================
    {
        "tenant_code": None,
        "role": "Auditor",
        "type": "sidebar",
        "device": "desktop",
        "app": "cbs",
        "items": [
            {"action_type": "page", "target": "cbs.auditor.dashboard", "icon": "home", "route": "/cbs/dashboard", "label": "Dashboard"},
            {"action_type": "page", "target": "cbs.audit.transactions", "icon": "file-text", "route": "/cbs/transactions", "label": "Transactions"},
            {"action_type": "page", "target": "cbs.audit.loans", "icon": "credit-card", "route": "/cbs/loans", "label": "Loans"},
            {"action_type": "page", "target": "cbs.audit.reports", "icon": "bar-chart", "route": "/cbs/reports", "label": "Reports"},
        ],
    },
]