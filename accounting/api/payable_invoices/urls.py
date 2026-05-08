# accounting/api/payable_invoices/urls.py

from django.urls import path

from .views import (
    PayableInvoiceListAPIView,
    PayableInvoiceCreateAPIView,
    PayableInvoiceDetailAPIView,
)

urlpatterns = [

    path(
        "",
        PayableInvoiceListAPIView.as_view()
    ),

    path(
        "create/",
        PayableInvoiceCreateAPIView.as_view()
    ),

    path(
        "<uuid:invoice_id>/",
        PayableInvoiceDetailAPIView.as_view()
    ),

]