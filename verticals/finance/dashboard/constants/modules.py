# verticals/finance/dashboard/constants/modules.py

journal = {
    "id": "journal",
    "title": "Journal",
    "icon": "receipt",
    "color": "linear-gradient(135deg, #1E3A8A, #2563EB)",
    "to": "/admin/finance/journals",
}

accounts = {
    "id": "accounts",
    "title": "Accounts",
    "icon": "spreadsheet",
    "color": "linear-gradient(135deg, #0F766E, #14B8A6)",
    "to": "/admin/finance/accounts",
}


# ====================================================
# RECEIVABLES (AR)
# ====================================================
ar_invoices = {
    "id": "ar_invoices",
    "title": "AR Invoices",
    "icon": "invoice",
    "color": "linear-gradient(135deg, #BE123C, #E11D48)",
    "to": "/finance/receivables/invoices",
}

ar_payments = {
    "id": "ar_payments",
    "title": "AR Payments",
    "icon": "payment",
    "color": "linear-gradient(135deg, #0369A1, #0EA5E9)",
    "to": "/finance/receivables/payments",
}

ar_dashboard = {
    "id": "ar_dashboard",
    "title": "AR Dashboard",
    "icon": "dashboard",
    "color": "linear-gradient(135deg, #15803D, #22C55E)",
    "to": "/finance/receivables/dashboard",
}

# ====================================================
# PAYABLES (AP)
# ====================================================
ap_invoices = {
    "id": "ap_invoices",
    "title": "AP Invoices",
    "icon": "invoice",
    "color": "linear-gradient(135deg, #BE123C, #E11D48)",
    "to": "/finance/payables/invoices",
}

ap_payments = {
    "id": "ap_payments",
    "title": "AP Payments",
    "icon": "payment",
    "color": "linear-gradient(135deg, #334155, #64748B)",
    "to": "/finance/payables/payments",
}

ap_dashboard = {
    "id": "ap_dashboard",
    "title": "AP Dashboard",
    "icon": "dashboard",
    "color": "linear-gradient(135deg, #4338CA, #6366F1)",
    "to": "/finance/payables/dashboard",
}


# ====================================================
# FIXED ASSET
# ====================================================
fa = {
    "id": "fa",
    "title": "Assets",
    "icon": "building",
    "color": "linear-gradient(135deg, #EA580C, #F97316)",
    "badge": "New",
    "to": "/finance/fixed-assets/",
}

fa_dashboard = {
    "id": "fa_dashboard",
    "title": "FA Dashboard",
    "icon": "dashboard",
    "color": "linear-gradient(135deg, #EA580C, #F97316)",
    "to": "/finance/fixed-assets/dashboard",
}

fa_depreciation = {
    "id": "fa_depreciation",
    "title": "FA Depreciation",
    "icon": "depreciation",
    "color": "linear-gradient(135deg, #EA580C, #F97316)",
    "to": "/finance/fixed-assets/depreciation",
}

fa_disposals = {
    "id": "fa_disposals",
    "title": "FA Disposals",
    "icon": "disposals",
    "color": "linear-gradient(135deg, #4338CA, #6366F1)",
    "to": "/finance/fixed-assets/disposals",
}

fa_categories = {
    "id": "fa_categories",
    "title": "FA Categories",
    "icon": "categories",
    "color": "linear-gradient(135deg, #BE123C, #E11D48)",
    "to": "/finance/fixed-assets/categories",
}

# ====================================================
# ACCOUNTING REPORTS
# ====================================================
trial_balance = {
    "id": "trial_balance",
    "title": "Trial Balance",
    "icon": "report",
    "color": "linear-gradient(135deg, #BE123C, #E11D48)",
    "to": "/admin/finance/reports/trial-balance",
}

profit_loss = {
    "id": "profit_loss",
    "title": "Profit Loss",
    "icon": "report",
    "color": "linear-gradient(135deg, #BE123C, #E11D48)",
    "to": "/admin/finance/reports/profit-loss",
}
balance_sheet = {
    "id": "balance_sheet",
    "title": "Balance Sheet",
    "icon": "report",
    "color": "linear-gradient(135deg, #BE123C, #E11D48)",
    "to": "/admin/finance/reports/balance-sheet",
}

cash_flow = {
    "id": "cash_flow",
    "title": "Cash Flow",
    "icon": "report",
    "color": "linear-gradient(135deg, #BE123C, #E11D48)",
    "to": "/admin/finance/reports/cash-flow",
}
