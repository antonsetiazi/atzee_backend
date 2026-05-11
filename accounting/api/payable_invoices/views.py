# accounting/api/payable_invoices/views.py

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import PayableInvoice
from accounting.services.payable_service import PayableService
from core.tenants.services import TenantService

from .serializers import (
    PayableInvoiceCreateSerializer,
    PayableInvoiceSerializer,
)


class PayableInvoiceListAPIView(APIView):
    def get(self, request):

        tenant = TenantService.get_current_tenant(request)
        qs = PayableInvoice.objects.filter(tenant=tenant)

        partner_id = request.GET.get("partner")

        if partner_id:
            qs = qs.filter(partner_id=partner_id)

        status_filter = request.GET.get("status")

        if status_filter:
            qs = qs.filter(status=status_filter)

        qs = qs.order_by("-invoice_date", "-created_at")[:100]

        data = PayableInvoiceSerializer(qs, many=True).data

        return Response(data)


class PayableInvoiceCreateAPIView(APIView):
    def post(self, request):

        try:
            tenant = TenantService.get_current_tenant(request)
            serializer = PayableInvoiceCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            invoice = PayableService.create_invoice(
                tenant=tenant,
                user=request.user,
                partner_id=serializer.validated_data["partner_id"],
                invoice_number=serializer.validated_data["invoice_number"],
                invoice_date=serializer.validated_data["invoice_date"],
                due_date=serializer.validated_data["due_date"],
                notes=serializer.validated_data.get("notes", ""),
                items=serializer.validated_data["items"],
                tax_id=serializer.validated_data.get("tax_id"),
            )

            output = PayableInvoiceSerializer(invoice)

            return Response(output.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class PayableInvoiceDetailAPIView(APIView):
    def get(self, request, invoice_id):

        try:
            tenant = TenantService.get_current_tenant(request)
            invoice = PayableInvoice.objects.get(id=invoice_id, tenant=tenant)

            data = PayableInvoiceSerializer(invoice).data

            return Response(data)

        except PayableInvoice.DoesNotExist:
            return Response(
                {"error": "Invoice not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class PayableInvoicePostAPIView(APIView):
    def post(self, request, invoice_id):
        tenant = TenantService.get_current_tenant(request)
        invoice = get_object_or_404(
            PayableInvoice,
            id=invoice_id,
            tenant=tenant,
        )

        try:

            invoice = PayableService.post_invoice(
                invoice=invoice,
                user=request.user,
            )

            data = PayableInvoiceSerializer(invoice).data

            return Response(data)

        except Exception as e:

            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class OutstandingPayableInvoiceListAPIView(APIView):
    def get(self, request):

        tenant = TenantService.get_current_tenant(request)

        qs = (
            PayableInvoice.objects.filter(
                tenant=tenant,
                status="posted",
                balance_due__gt=0,
            )
            .select_related("partner")
            .order_by("-invoice_date")
        )

        data = []
        for obj in qs:
            data.append(
                {
                    "id": str(obj.id),
                    "partner_id": obj.partner.id,
                    "invoice_number": obj.invoice_number,
                    "partner_name": obj.partner.name,
                    "total_amount": obj.total_amount,
                    "paid_amount": obj.paid_amount,
                    "balance_due": obj.balance_due,
                }
            )

        return Response(data)
