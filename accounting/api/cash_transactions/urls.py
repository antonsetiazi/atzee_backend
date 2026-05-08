# accounting/api/cash_transactions/urls.py

from django.urls import path

from .views import (
    CashTransactionListAPIView,
    CashInAPIView,
    CashOutAPIView,
    TransferAPIView,
)

urlpatterns = [

    path(
        "",
        CashTransactionListAPIView.as_view()
    ),

    path(
        "cash-in/",
        CashInAPIView.as_view()
    ),

    path(
        "cash-out/",
        CashOutAPIView.as_view()
    ),

    path(
        "transfer/",
        TransferAPIView.as_view()
    ),

]