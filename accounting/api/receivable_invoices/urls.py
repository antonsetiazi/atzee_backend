# accounting/api/receivable_invoices/urls.py

from django.urls import path

from .views import (
    ReceivableInvoiceListAPIView,
    ReceivableInvoiceCreateAPIView,
    ReceivableInvoiceDetailAPIView,
)

urlpatterns = [

    path(
        "",
        ReceivableInvoiceListAPIView.as_view()
    ),

    path(
        "create/",
        ReceivableInvoiceCreateAPIView.as_view()
    ),

    path(
        "<uuid:invoice_id>/",
        ReceivableInvoiceDetailAPIView.as_view()
    ),
]