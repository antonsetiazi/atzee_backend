# hrms/api/dashboard/views.py

from rest_framework.response import Response
from rest_framework.views import APIView

from hrms.selectors import (
    get_hrms_dashboard_summary,
)


class HRMSDashboardApi(APIView):

    def get(self, request):

        summary = get_hrms_dashboard_summary(
            tenant=request.user.tenant,
        )

        return Response(summary)
