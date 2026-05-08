# accounting/api/payable_payments/urls.py

from django.urls import path

from .views import (
    PayablePaymentListAPIView,
    PayablePaymentCreateAPIView,
    PayablePaymentDetailAPIView,
)

urlpatterns = [

    path(
        "",
        PayablePaymentListAPIView.as_view()
    ),

    path(
        "create/",
        PayablePaymentCreateAPIView.as_view()
    ),

    path(
        "<uuid:payment_id>/",
        PayablePaymentDetailAPIView.as_view()
    ),

]