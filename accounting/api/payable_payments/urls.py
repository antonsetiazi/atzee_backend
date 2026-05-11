# accounting/api/payable_payments/urls.py

from django.urls import path

from .views import (
    PayablePaymentCreateAPIView,
    PayablePaymentDetailAPIView,
    PayablePaymentListAPIView,
    PayablePaymentPostAPIView,
)

urlpatterns = [
    path("", PayablePaymentListAPIView.as_view()),
    path("create/", PayablePaymentCreateAPIView.as_view()),
    path("<uuid:payment_id>/", PayablePaymentDetailAPIView.as_view()),
    path("<uuid:payment_id>/post/", PayablePaymentPostAPIView.as_view()),
]
