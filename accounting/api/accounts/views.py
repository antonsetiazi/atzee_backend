# accounting/api/accounts/views.py

from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import Account
from core.tenants.services import TenantService


class AccountListAPIView(APIView):

    def get(self, request):

        tenant = TenantService.get_current_tenant(request)
        qs = Account.objects.filter(tenant=tenant)

        return Response(
            [
                {
                    "id": a.id,
                    "code": a.code,
                    "name": a.name,
                }
                for a in qs
            ]
        )
