# accounting/api/cash_bank_accounts/urls.py

from django.urls import path

from .views import (
    CashBankAccountCreateAPIView,
    CashBankAccountDetailAPIView,
    CashBankAccountListAPIView,
    CashBankAccountOptionsAPIView,
)

urlpatterns = [
    path("", CashBankAccountListAPIView.as_view()),
    path("create/", CashBankAccountCreateAPIView.as_view()),
    path("<uuid:account_id>/", CashBankAccountDetailAPIView.as_view()),
    path("options/", CashBankAccountOptionsAPIView.as_view()),
]
