# accounting/api/receivable_invoices/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounting.models import ReceivableInvoice

from accounting.services.receivable_service import (
    ReceivableService
)

from .serializers import (
    ReceivableInvoiceSerializer
)


class ReceivableInvoiceListAPIView(APIView):

    def get(self, request):

        qs = ReceivableInvoice.objects.filter(
            tenant=request.user.tenant
        )

        customer_id = request.GET.get("customer")
        status_filter = request.GET.get("status")

        if customer_id:
            qs = qs.filter(customer_id=customer_id)

        if status_filter:
            qs = qs.filter(status=status_filter)

        qs = qs.order_by(
            "-invoice_date",
            "-created_at"
        )[:100]

        data = ReceivableInvoiceSerializer(
            qs,
            many=True
        ).data

        return Response(data)


class ReceivableInvoiceCreateAPIView(APIView):

    def post(self, request):

        try:

            serializer = ReceivableInvoiceSerializer(
                data=request.data
            )

            serializer.is_valid(raise_exception=True)

            invoice = ReceivableService.create_invoice(
                tenant=request.user.tenant,
                user=request.user,

                customer_id=serializer.validated_data[
                    "customer"
                ].id,

                invoice_number=serializer.validated_data[
                    "invoice_number"
                ],

                invoice_date=serializer.validated_data[
                    "invoice_date"
                ],

                due_date=serializer.validated_data[
                    "due_date"
                ],

                notes=serializer.validated_data.get(
                    "notes",
                    ""
                ),

                items=serializer.validated_data[
                    "items"
                ],
            )

            output = ReceivableInvoiceSerializer(
                invoice
            )

            return Response(
                output.data,
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class ReceivableInvoiceDetailAPIView(APIView):

    def get(self, request, invoice_id):

        try:

            invoice = ReceivableInvoice.objects.get(
                id=invoice_id,
                tenant=request.user.tenant
            )

            data = ReceivableInvoiceSerializer(
                invoice
            ).data

            return Response(data)

        except ReceivableInvoice.DoesNotExist:

            return Response(
                {
                    "error": "Invoice not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )