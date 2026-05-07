# accounting/api/reports/profit_loss.py

from rest_framework.views import APIView
from rest_framework.response import Response

from accounting.services.report_service import ReportService


class ProfitLossAPIView(APIView):

    def get(self, request):
        tenant = request.user.tenant

        date_from = request.GET.get("date_from")
        date_to = request.GET.get("date_to")

        data = ReportService.get_profit_loss(
            tenant=tenant,
            date_from=date_from,
            date_to=date_to
        )

        return Response(data)