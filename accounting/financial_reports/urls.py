from django.urls import path
from accounting.financial_reports.views import (
    TrialBalanceView,
    ProfitLossView,
    BalanceSheetView
)

urlpatterns = [
    path("trial-balance", TrialBalanceView.as_view()),
    path("profit-loss", ProfitLossView.as_view()),
    path("balance-sheet", BalanceSheetView.as_view()),
]
