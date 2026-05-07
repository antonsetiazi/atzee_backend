# accounting/api/receivable_payments/urls.py

from django.urls import path

from .views import (
    ReceivablePaymentListAPIView,
    ReceivablePaymentCreateAPIView,
    ReceivablePaymentDetailAPIView,
)

urlpatterns = [

    path(
        "",
        ReceivablePaymentListAPIView.as_view()
    ),

    path(
        "create/",
        ReceivablePaymentCreateAPIView.as_view()
    ),

    path(
        "<uuid:payment_id>/",
        ReceivablePaymentDetailAPIView.as_view()
    ),
]