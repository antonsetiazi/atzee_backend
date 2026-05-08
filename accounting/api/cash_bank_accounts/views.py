# accounting/api/cash_bank_accounts/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import CashBankAccount
from core.tenants.services import TenantService

from .serializers import CashBankAccountSerializer


class CashBankAccountListAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)
        qs = CashBankAccount.objects.filter(tenant=tenant)

        data = CashBankAccountSerializer(qs, many=True).data

        return Response(data)


class CashBankAccountCreateAPIView(APIView):

    def post(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = CashBankAccountSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        obj = serializer.save(
            tenant=tenant,
            created_by=request.user,
        )

        return Response(
            CashBankAccountSerializer(obj).data, status=status.HTTP_201_CREATED
        )


class CashBankAccountDetailAPIView(APIView):

    def get(self, request, account_id):

        try:
            tenant = TenantService.get_current_tenant(request)
            obj = CashBankAccount.objects.get(id=account_id, tenant=tenant)

            data = CashBankAccountSerializer(obj).data

            return Response(data)

        except CashBankAccount.DoesNotExist:

            return Response(
                {"error": "Account not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CashBankAccountOptionsAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        qs = CashBankAccount.objects.filter(
            tenant=tenant, is_active=True
        ).order_by("name")

        data = [
            {
                "id": str(obj.id),
                "name": obj.name,
                "account_number": obj.bank_account_number,
            }
            for obj in qs
        ]

        return Response(data)
