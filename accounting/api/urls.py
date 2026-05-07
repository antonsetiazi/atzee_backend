# accounting/api/urls.py

from django.urls import path, include

urlpatterns = [

    path(
        "journals/",
        include("accounting.api.journals.urls")
    ),

    path(
        "reports/",
        include("accounting.api.reports.urls")
    ),

    path(
        "receivable-invoices/",
        include(
            "accounting.api.receivable_invoices.urls"
        )
    ),

    path(
        "receivable-payments/",
        include(
            "accounting.api.receivable_payments.urls"
        )
    ),

    path(
        "receivable-aging/",
        include(
            "accounting.api.receivable_aging.urls"
        )
    ),

]