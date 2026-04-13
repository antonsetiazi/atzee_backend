# core/wallet_withdrawal/api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from core.wallet_withdrawal.services.withdrawal_service import request_withdrawal
from core.wallet_withdrawal.selectors.withdrawal_selectors import (
    get_user_withdrawals,
    get_withdrawal_by_id,
)
from core.wallet_withdrawal.api.serializers import (
    WithdrawalRequestSerializer,
    WithdrawalSerializer,
)


class WithdrawalCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tenant = TenantService.get_current_tenant(request)

        serializer = WithdrawalRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        withdrawal = request_withdrawal(
            tenant=tenant,
            user=request.user,
            amount=serializer.validated_data["amount"],
            destination=serializer.validated_data["destination"],
        )

        return Response(WithdrawalSerializer(withdrawal).data)


class WithdrawalListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        withdrawals = get_user_withdrawals(
            tenant=tenant,
            user=request.user
        )
        return Response(WithdrawalSerializer(withdrawals, many=True).data)


class WithdrawalDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, withdrawal_id):
        tenant = TenantService.get_current_tenant(request)

        withdrawal = get_withdrawal_by_id(
            tenant=tenant,
            user=request.user,
            withdrawal_id=withdrawal_id
        )

        if not withdrawal:
            return Response({"detail": "Not found"}, status=404)

        return Response(WithdrawalSerializer(withdrawal).data)