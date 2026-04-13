# core/wallet_withdrawal/api/urls.py

from django.urls import path
from .views import (
    WithdrawalCreateAPIView,
    WithdrawalListAPIView,
    WithdrawalDetailAPIView,
)

urlpatterns = [
    path("withdrawals/", WithdrawalListAPIView.as_view()),
    path("withdrawals/create/", WithdrawalCreateAPIView.as_view()),
    path("withdrawals/<uuid:withdrawal_id>/", WithdrawalDetailAPIView.as_view()),
]