from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounting.chart_of_accounts import selectors
from accounting.chart_of_accounts.serializers import (
    AccountListSerializer,
    AccountDetailSerializer,
    AccountCreateSerializer,
)


class ChartOfAccountViewSet(viewsets.ViewSet):
    """
    Chart of Accounts API (tenant scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        accounts = selectors.get_accounts(
            tenant=request.tenant
        )
        serializer = AccountListSerializer(accounts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        account = selectors.get_account_by_id(
            tenant=request.tenant,
            account_id=pk
        )

        if not account:
            return Response(
                {"detail": "Account not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AccountDetailSerializer(account)
        return Response(serializer.data)

    def create(self, request):
        serializer = AccountCreateSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        account = serializer.save()

        output = AccountDetailSerializer(account)
        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )
