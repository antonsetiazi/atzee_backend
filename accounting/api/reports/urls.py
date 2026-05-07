# accounting/api/reports/urls.py

from django.urls import path

from .trial_balance import TrialBalanceAPIView
from .profit_loss import ProfitLossAPIView
from .balance_sheet import BalanceSheetAPIView

urlpatterns = [
    path(
        "trial-balance/",
        TrialBalanceAPIView.as_view()
    ),

    path(
        "profit-loss/",
        ProfitLossAPIView.as_view()
    ),

    path(
        "balance-sheet/",
        BalanceSheetAPIView.as_view()
    ),
]