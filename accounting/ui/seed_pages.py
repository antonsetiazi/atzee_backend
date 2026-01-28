# accounting/ui/seed_pages.py

UI_PAGES = [
    # =====================
    # CHART OF ACCOUNTS
    # =====================
    {
        "key": "chart_of_accounts.list",
        "entity": "chart_of_accounts",
        "title": "Chart of Accounts",
        "permissions": ["accounting.chart_of_accounts.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/accounting/chart-of-accounts/",
                "columns": [
                    {"key": "code", "label": "Account Code"},
                    {"key": "name", "label": "Account Name"},
                    {"key": "type", "label": "Type"},
                    {"key": "balance", "label": "Balance"},
                ],
            }
        ],
    },

    # =====================
    # JOURNALS
    # =====================
    {
        "key": "journals.list",
        "entity": "journals",
        "title": "Journals",
        "permissions": ["accounting.journals.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/accounting/journals/",
                "columns": [
                    {"key": "date", "label": "Date"},
                    {"key": "reference", "label": "Reference"},
                    {"key": "description", "label": "Description"},
                    {"key": "total_debit", "label": "Debit"},
                    {"key": "total_credit", "label": "Credit"},
                ],
            }
        ],
    },

    # =====================
    # LEDGER
    # =====================
    {
        "key": "ledger.list",
        "entity": "ledger",
        "title": "Ledger",
        "permissions": ["accounting.ledger.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/accounting/ledger/",
                "columns": [
                    {"key": "account", "label": "Account"},
                    {"key": "date", "label": "Date"},
                    {"key": "debit", "label": "Debit"},
                    {"key": "credit", "label": "Credit"},
                    {"key": "balance", "label": "Balance"},
                ],
            }
        ],
    },

    # =====================
    # FISCAL PERIODS
    # =====================
    {
        "key": "fiscal_period.list",
        "entity": "fiscal_period",
        "title": "Fiscal Periods",
        "permissions": ["accounting.fiscal_period.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/accounting/fiscal-periods/",
                "columns": [
                    {"key": "name", "label": "Period Name"},
                    {"key": "start_date", "label": "Start Date"},
                    {"key": "end_date", "label": "End Date"},
                    {"key": "is_closed", "label": "Closed"},
                ],
            }
        ],
    },

    # =====================
    # TAXES
    # =====================
    {
        "key": "taxes.list",
        "entity": "taxes",
        "title": "Taxes",
        "permissions": ["accounting.taxes.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/accounting/taxes/",
                "columns": [
                    {"key": "name", "label": "Tax Name"},
                    {"key": "rate", "label": "Rate (%)"},
                    {"key": "is_active", "label": "Active"},
                ],
            }
        ],
    },

    # =====================
    # FINANCIAL REPORTS
    # =====================
    {
        "key": "financial_reports.list",
        "entity": "financial_reports",
        "title": "Financial Reports",
        "permissions": ["accounting.financial_reports.view"],
        "blocks": [
            {
                "type": "table",
                "data_source": "/api/accounting/financial-reports/",
                "columns": [
                    {"key": "name", "label": "Report Name"},
                    {"key": "period", "label": "Period"},
                    {"key": "generated_at", "label": "Generated At"},
                    {"key": "status", "label": "Status"},
                ],
            }
        ],
    },
]
