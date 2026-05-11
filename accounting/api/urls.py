# accounting/api/urls.py

from django.urls import include, path

urlpatterns = [
    path("accounts/", include("accounting.api.accounts.urls")),
    path("journals/", include("accounting.api.journals.urls")),
    path("reports/", include("accounting.api.reports.urls")),
    path(
        "receivable-invoices/",
        include("accounting.api.receivable_invoices.urls"),
    ),
    path(
        "receivable-payments/",
        include("accounting.api.receivable_payments.urls"),
    ),
    path("receivable-aging/", include("accounting.api.receivable_aging.urls")),
    path("payable-invoices/", include("accounting.api.payable_invoices.urls")),
    path("payable-payments/", include("accounting.api.payable_payments.urls")),
    path(
        "payables/dashboard/",
        include("accounting.api.payables_dashboard.urls"),
    ),
    path(
        "cash-bank-accounts/",
        include("accounting.api.cash_bank_accounts.urls"),
    ),
    path(
        "cash-transactions/", include("accounting.api.cash_transactions.urls")
    ),
    path("taxes/", include("accounting.api.taxes.urls")),
    path(
        "receivables/dashboard/",
        include("accounting.api.receivables_dashboard.urls"),
    ),
    path(
        "asset-categories/",
        include("accounting.api.asset_categories.urls"),
    ),
    path(
        "fixed-assets/",
        include("accounting.api.fixed_assets.urls"),
    ),
    path(
        "fixed-asset-depreciation/",
        include("accounting.api.fixed_asset_depreciation.urls"),
    ),
    path(
        "asset-disposals/",
        include("accounting.api.asset_disposals.urls"),
    ),
    path(
        "fixed-assets-dashboard/",
        include("accounting.api.fixed_assets_dashboard.urls"),
    ),
]
