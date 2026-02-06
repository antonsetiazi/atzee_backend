from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.tenants.services import TenantService
from accounting.chart_of_accounts import selectors, services
from accounting.chart_of_accounts.serializers import (
    AccountListSerializer,
    AccountDetailSerializer,
    AccountCreateSerializer,
    AccountUpdateSerializer
)


class ChartOfAccountViewSet(viewsets.ViewSet):
    """
    Chart of Accounts API (tenant scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        accounts = selectors.get_accounts(tenant=tenant)
        serializer = AccountListSerializer(accounts, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        print("retrieve")
        tenant = TenantService.get_current_tenant(request)
        print('1')
        account = selectors.get_account_by_id(tenant=tenant, account_id=pk)
        print('2')

        if not account:
            return Response(
                {"detail": "Account not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AccountDetailSerializer(account)
        return Response(serializer.data)

    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = AccountCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = services.create_account(
            tenant=tenant,
            created_by=request.user,
            **serializer.validated_data
        )
        output = AccountDetailSerializer(account)
        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )


    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        account = selectors.get_account_by_id(tenant=tenant, account_id=pk)

        if not account:
            return Response(
                {"detail": "Account not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = AccountUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        account = services.update_account(
            tenant=tenant,
            account_id=account.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = AccountDetailSerializer(account)
        return Response(output.data)
    

    def partial_update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        account = selectors.get_account_by_id(tenant=tenant, account_id=pk)

        if not account:
            return Response(
                {"detail": "Account not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = AccountUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        account = services.update_account(
            tenant=tenant,
            account_id=account.id,
            updated_by=request.user,
            **serializer.validated_data
        )

        output = AccountDetailSerializer(account)
        return Response(output.data)
    

    def destroy(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)

        services.delete_account(
            tenant=tenant,
            account_id=pk,
            deleted_by=request.user
        )

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )