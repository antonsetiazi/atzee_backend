# accounting/api/receivable_aging/views.py

from rest_framework.views import APIView
from rest_framework.response import Response

from accounting.services.aging_receivable_service import (
    AgingReceivableService
)


class ReceivableAgingAPIView(APIView):

    def get(self, request):

        data = AgingReceivableService.generate(
            tenant=request.user.tenant
        )

        return Response(data)