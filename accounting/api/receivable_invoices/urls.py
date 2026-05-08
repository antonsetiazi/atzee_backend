# accounting/api/receivable_invoices/urls.py

from django.urls import path

from .views import (
    OutstandingInvoiceListAPIView,
    ReceivableInvoiceCreateAPIView,
    ReceivableInvoiceDetailAPIView,
    ReceivableInvoiceListAPIView,
    ReceivableInvoicePostAPIView,
)

urlpatterns = [
    path("", ReceivableInvoiceListAPIView.as_view()),
    path("create/", ReceivableInvoiceCreateAPIView.as_view()),
    path("<uuid:invoice_id>/", ReceivableInvoiceDetailAPIView.as_view()),
    path("<uuid:invoice_id>/post/", ReceivableInvoicePostAPIView.as_view()),
    path("outstanding/", OutstandingInvoiceListAPIView.as_view()),
]
