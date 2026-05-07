# accounting/api/reports/trial_balance.py

from rest_framework.views import APIView
from rest_framework.response import Response

from accounting.services.report_service import ReportService


class TrialBalanceAPIView(APIView):

    def get(self, request):
        tenant = request.user.tenant

        date_from = request.GET.get("date_from")
        date_to = request.GET.get("date_to")

        data = ReportService.get_trial_balance(
            tenant=tenant,
            date_from=date_from,
            date_to=date_to
        )

        return Response(data)