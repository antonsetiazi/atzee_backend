# business/transactions/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from core.tenants.services import TenantService
from business.transactions import selectors, services
from business.transactions.models.transaction import Transaction
from business.transactions.serializers import (
    TransactionListSerializer,
    TransactionDetailSerializer,
    TransactionCreateSerializer,
    TransactionUpdateSerializer,
    TransactionItemAddSerializer,
    TransactionItemUpdateSerializer,
    TransactionConfirmSerializer,
    TransactionCancelSerializer,
)

from business.transactions.models.enums import (
    TransactionType,
    TransactionSubType,
    TransactionStatus,
)

from business.customers.selectors import get_customer_by_id
from business.products.selectors import get_product_by_id

class TransactionViewSet(viewsets.ViewSet):
    """
    Transaction API endpoints (tenant scoped).
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tenant = TenantService.get_current_tenant(request)
        transactions = selectors.get_transactions(tenant=tenant)
        serializer = TransactionListSerializer(transactions, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        transaction = selectors.get_transaction_by_id(tenant=tenant, transaction_id=pk)

        if not transaction:
            return Response(
                {"detail": "Transaction not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TransactionDetailSerializer(transaction)
        return Response(serializer.data)


    def create(self, request):
        tenant = TenantService.get_current_tenant(request)
        serializer = TransactionCreateSerializer(
            data=request.data,
            context={
                "request": request,
                "transaction_type": TransactionType.SALES,
                "subtype": TransactionSubType.DIRECT,
            }
        )
        
        serializer.is_valid(raise_exception=True)
        
        data  = serializer.validated_data

        transaction = services.create_transaction(
            tenant=tenant,
            created_by=request.user,
            transaction_type=TransactionType.SALES,
            subtype=TransactionSubType.DIRECT,
            reference=data.get("reference") or services.generate_sales_reference(tenant),
            transaction_date=data["transaction_date"],
            customer=get_customer_by_id(
                tenant=tenant,
                customer_id=data.get("customer_id"),
            ),
            notes=data.get("notes"),
        )

        output = TransactionDetailSerializer(transaction)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )


    def update(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        transaction = selectors.get_transaction_by_id(tenant=tenant, transaction_id=pk)

        if not transaction:
            return Response(
                {"detail": "Transaction not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = TransactionUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        transaction = services.update_transaction(
            tenant=tenant,
            transaction_id=transaction.id,
            updated_by=request.user,
            **serializer.validated_data
        )
        
        output = TransactionDetailSerializer(transaction)

        return Response(output.data)
    
    @action(
        detail=True,
        methods=["post"],
        url_path="items"
    )
    def add_item(self, request, pk=None):
        try:
            tenant = TenantService.get_current_tenant(request)
            transaction = selectors.get_transaction_by_id(tenant=tenant, transaction_id=pk)
    
            if not transaction:
                return Response(
                    {"detail": "Transaction not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = TransactionItemAddSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data  = serializer.validated_data

            product = get_product_by_id(
                tenant=tenant,
                product_id=data.get("product_id"),
            )

            if not product:
                return Response(
                    {"detail": "Product not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

            services.add_transaction_item(
                tenant=tenant,
                created_by=request.user,
                transaction_id=transaction.id,
                product=product,
                quantity=data.get("quantity"),
                unit_price=data.get("unit_price"),
                notes=data.get("notes")
            )

            # ⬇️ refresh supaya items ter-load ulang
            transaction.refresh_from_db()

            output = TransactionDetailSerializer(transaction)
            return Response(output.data)
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


    # PATCH /api/business/transactions/{transaction_id}/items/{item_id}/
    @action(
        detail=True,
        methods=["patch"],
        url_path="items/(?P<item_id>[^/.]+)"
    )
    def update_item(self, request, pk=None, item_id=None):
        tenant = TenantService.get_current_tenant(request)
        transaction = selectors.get_transaction_by_id(
            tenant=tenant,
            transaction_id=pk
        )

        if not transaction:
            return Response(
                {"detail": "Transaction not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TransactionItemUpdateSerializer(
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)

        services.update_transaction_item(
            tenant=tenant,
            transaction_id=transaction.id,
            item_id=item_id,
            updated_by=request.user,
            **serializer.validated_data
        )

        # refresh aggregate
        transaction.refresh_from_db()

        output = TransactionDetailSerializer(transaction)
        return Response(output.data)


    # DELETE /api/business/transactions/{transaction_id}/items/{item_id}/
    @action(
        detail=True,
        methods=["delete"],
        url_path="items/(?P<item_id>[^/.]+)"
    )
    def destroy_item(self, request, pk=None, item_id=None):
        tenant = TenantService.get_current_tenant(request)

        transaction = selectors.get_transaction_by_id(
            tenant=tenant,
            transaction_id=pk
        )

        if not transaction:
            return Response(
                {"detail": "Transaction not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # ⬇️ delegasikan ke service (biar domain logic tetap bersih)
        services.remove_transaction_item(
            tenant=tenant,
            transaction_id=transaction.id,
            item_id=item_id,
            deleted_by=request.user,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(
        detail=True,
        methods=["post"],
        url_path="confirm"
    )
    def confirm(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        transaction = selectors.get_transaction_by_id(tenant=tenant, transaction_id=pk)

        if not transaction:
            return Response(
                {"detail": "Transaction not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TransactionConfirmSerializer(
            data={},
            context={
                "request": request,
                "transaction": transaction,
            }
        )
        serializer.is_valid(raise_exception=True)

        transaction = serializer.save()

        output = TransactionDetailSerializer(transaction)
        return Response(output.data)


    @action(
        detail=True,
        methods=["post"],
        url_path="cancel"
    )
    def cancel(self, request, pk=None):
        tenant = TenantService.get_current_tenant(request)
        transaction = selectors.get_transaction_by_id(tenant=tenant, transaction_id=pk)

        if not transaction:
            return Response(
                {"detail": "Transaction not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TransactionCancelSerializer(
            data=request.data,
            context={
                "request": request,
                "transaction": transaction,
            }
        )
        serializer.is_valid(raise_exception=True)

        transaction = serializer.save()

        output = TransactionDetailSerializer(transaction)
        return Response(output.data)
