# accounting/api/reports/balance_sheet.py

from rest_framework.views import APIView
from rest_framework.response import Response

from accounting.services.report_service import ReportService


class BalanceSheetAPIView(APIView):

    def get(self, request):
        tenant = request.user.tenant

        date_to = request.GET.get("date_to")

        data = ReportService.get_balance_sheet(
            tenant=tenant,
            date_to=date_to
        )

        return Response(data)