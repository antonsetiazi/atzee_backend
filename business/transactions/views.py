from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from business.transactions import selectors
from business.transactions.models.transaction import Transaction
from business.transactions.serializers import (
    TransactionListSerializer,
    TransactionDetailSerializer,
    TransactionCreateSerializer,
    TransactionItemAddSerializer,
    TransactionConfirmSerializer,
    TransactionCancelSerializer,
)


class TransactionViewSet(viewsets.ViewSet):
    """
    Transaction API endpoints (tenant scoped).
    """

    permission_classes = [IsAuthenticated]


    def list(self, request):
        transactions = selectors.get_transactions(
            tenant=request.tenant
        )

        serializer = TransactionListSerializer(transactions, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        transaction = selectors.get_transaction_by_id(
            tenant=request.tenant,
            transaction_id=pk
        )

        if not transaction:
            return Response(
                {"detail": "Transaction not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TransactionDetailSerializer(transaction)
        return Response(serializer.data)


    def create(self, request):
        serializer = TransactionCreateSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        transaction = serializer.save()

        output = TransactionDetailSerializer(transaction)
        return Response(
            output.data,
            status=status.HTTP_201_CREATED
        )


    @action(
        detail=True,
        methods=["post"],
        url_path="add-item"
    )
    def add_item(self, request, pk=None):
        transaction = selectors.get_transaction_by_id(
            tenant=request.tenant,
            transaction_id=pk
        )

        if not transaction:
            return Response(
                {"detail": "Transaction not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TransactionItemAddSerializer(
            data=request.data,
            context={
                "request": request,
                "transaction": transaction,
            }
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()

        output = TransactionDetailSerializer(transaction)
        return Response(output.data)


    @action(
        detail=True,
        methods=["post"],
        url_path="confirm"
    )
    def confirm(self, request, pk=None):
        transaction = selectors.get_transaction_by_id(
            tenant=request.tenant,
            transaction_id=pk
        )

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
        transaction = selectors.get_transaction_by_id(
            tenant=request.tenant,
            transaction_id=pk
        )

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
