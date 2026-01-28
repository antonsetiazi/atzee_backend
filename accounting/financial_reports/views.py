from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounting.financial_reports.selectors.trial_balance import get_trial_balance
from accounting.financial_reports.selectors.profit_loss import get_profit_and_loss
from accounting.financial_reports.selectors.balance_sheet import get_balance_sheet


class TrialBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_trial_balance(
            tenant=request.tenant,
            start_date=request.query_params.get("start_date"),
            end_date=request.query_params.get("end_date"),
        )
        return Response(data)


class ProfitLossView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_profit_and_loss(
            tenant=request.tenant,
            start_date=request.query_params.get("start_date"),
            end_date=request.query_params.get("end_date"),
        )
        return Response(data)


class BalanceSheetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_balance_sheet(
            tenant=request.tenant,
            as_of_date=request.query_params.get("as_of_date"),
        )
        return Response(data)