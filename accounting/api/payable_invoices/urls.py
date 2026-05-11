# accounting/api/payable_invoices/urls.py

from django.urls import path

from .views import (
    OutstandingPayableInvoiceListAPIView,
    PayableInvoiceCreateAPIView,
    PayableInvoiceDetailAPIView,
    PayableInvoiceListAPIView,
    PayableInvoicePostAPIView,
)

urlpatterns = [
    path("", PayableInvoiceListAPIView.as_view()),
    path("create/", PayableInvoiceCreateAPIView.as_view()),
    path("<uuid:invoice_id>/", PayableInvoiceDetailAPIView.as_view()),
    path("<uuid:invoice_id>/post/", PayableInvoicePostAPIView.as_view()),
    path("outstanding/", OutstandingPayableInvoiceListAPIView.as_view()),
]
