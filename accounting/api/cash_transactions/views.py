# accounting/api/cash_transactions/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounting.models import (
    CashTransaction
)

from accounting.services.cash_transaction_service import (
    CashTransactionService
)

from .serializers import (
    CashTransactionSerializer
)


class CashTransactionListAPIView(
    APIView
):

    def get(self, request):

        qs = CashTransaction.objects.filter(
            tenant=request.user.tenant
        )

        trx_type = request.GET.get(
            "transaction_type"
        )

        if trx_type:
            qs = qs.filter(
                transaction_type=trx_type
            )

        qs = qs.order_by(
            "-transaction_date",
            "-created_at"
        )[:100]

        data = CashTransactionSerializer(
            qs,
            many=True
        ).data

        return Response(data)


class CashInAPIView(APIView):

    def post(self, request):

        try:

            serializer = (
                CashTransactionSerializer(
                    data=request.data
                )
            )

            serializer.is_valid(
                raise_exception=True
            )

            trx = (
                CashTransactionService.create_cash_in(
                    tenant=request.user.tenant,
                    user=request.user,

                    transaction_number=serializer.validated_data[
                        "transaction_number"
                    ],

                    transaction_date=serializer.validated_data[
                        "transaction_date"
                    ],

                    to_account_id=serializer.validated_data[
                        "to_account"
                    ].id,

                    amount=serializer.validated_data[
                        "amount"
                    ],

                    reference=serializer.validated_data.get(
                        "reference",
                        ""
                    ),

                    description=serializer.validated_data.get(
                        "description",
                        ""
                    ),
                )
            )

            return Response(
                CashTransactionSerializer(
                    trx
                ).data,
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class CashOutAPIView(APIView):

    def post(self, request):

        try:

            serializer = (
                CashTransactionSerializer(
                    data=request.data
                )
            )

            serializer.is_valid(
                raise_exception=True
            )

            trx = (
                CashTransactionService.create_cash_out(
                    tenant=request.user.tenant,
                    user=request.user,

                    transaction_number=serializer.validated_data[
                        "transaction_number"
                    ],

                    transaction_date=serializer.validated_data[
                        "transaction_date"
                    ],

                    from_account_id=serializer.validated_data[
                        "from_account"
                    ].id,

                    amount=serializer.validated_data[
                        "amount"
                    ],

                    reference=serializer.validated_data.get(
                        "reference",
                        ""
                    ),

                    description=serializer.validated_data.get(
                        "description",
                        ""
                    ),
                )
            )

            return Response(
                CashTransactionSerializer(
                    trx
                ).data,
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class TransferAPIView(APIView):

    def post(self, request):

        try:

            serializer = (
                CashTransactionSerializer(
                    data=request.data
                )
            )

            serializer.is_valid(
                raise_exception=True
            )

            trx = (
                CashTransactionService.create_transfer(
                    tenant=request.user.tenant,
                    user=request.user,

                    transaction_number=serializer.validated_data[
                        "transaction_number"
                    ],

                    transaction_date=serializer.validated_data[
                        "transaction_date"
                    ],

                    from_account_id=serializer.validated_data[
                        "from_account"
                    ].id,

                    to_account_id=serializer.validated_data[
                        "to_account"
                    ].id,

                    amount=serializer.validated_data[
                        "amount"
                    ],

                    reference=serializer.validated_data.get(
                        "reference",
                        ""
                    ),

                    description=serializer.validated_data.get(
                        "description",
                        ""
                    ),
                )
            )

            return Response(
                CashTransactionSerializer(
                    trx
                ).data,
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )