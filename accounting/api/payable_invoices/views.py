# accounting/api/payable_invoices/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounting.models import (
    PayableInvoice
)

from accounting.services.payable_service import (
    PayableService
)

from .serializers import (
    PayableInvoiceSerializer
)


class PayableInvoiceListAPIView(APIView):

    def get(self, request):

        qs = PayableInvoice.objects.filter(
            tenant=request.user.tenant
        )

        partner_id = request.GET.get("partner")

        if partner_id:
            qs = qs.filter(
                partner_id=partner_id
            )

        status_filter = request.GET.get(
            "status"
        )

        if status_filter:
            qs = qs.filter(
                status=status_filter
            )

        qs = qs.order_by(
            "-invoice_date",
            "-created_at"
        )[:100]

        data = PayableInvoiceSerializer(
            qs,
            many=True
        ).data

        return Response(data)


class PayableInvoiceCreateAPIView(
    APIView
):

    def post(self, request):

        try:

            serializer = (
                PayableInvoiceSerializer(
                    data=request.data
                )
            )

            serializer.is_valid(
                raise_exception=True
            )

            invoice = (
                PayableService.create_invoice(
                    tenant=request.user.tenant,
                    user=request.user,

                    partner_id=serializer.validated_data[
                        "partner"
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
            )

            output = (
                PayableInvoiceSerializer(
                    invoice
                )
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


class PayableInvoiceDetailAPIView(
    APIView
):

    def get(self, request, invoice_id):

        try:

            invoice = (
                PayableInvoice.objects.get(
                    id=invoice_id,
                    tenant=request.user.tenant
                )
            )

            data = PayableInvoiceSerializer(
                invoice
            ).data

            return Response(data)

        except PayableInvoice.DoesNotExist:

            return Response(
                {
                    "error": "Invoice not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )