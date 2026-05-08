# accounting/api/receivable_invoices/views.py

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import ReceivableInvoice
from accounting.services.receivable_service import ReceivableService
from core.tenants.services import TenantService

from .serializers import (
    ReceivableInvoiceCreateSerializer,
    ReceivableInvoiceSerializer,
)


class ReceivableInvoiceListAPIView(APIView):

    def get(self, request):
        tenant = TenantService.get_current_tenant(request)

        qs = ReceivableInvoice.objects.filter(tenant=tenant)

        customer_id = request.GET.get("customer")
        status_filter = request.GET.get("status")

        if customer_id:
            qs = qs.filter(customer_id=customer_id)

        if status_filter:
            qs = qs.filter(status=status_filter)

        qs = qs.order_by("-invoice_date", "-created_at")[:100]

        data = ReceivableInvoiceSerializer(qs, many=True).data

        return Response(data)


class ReceivableInvoiceCreateAPIView(APIView):

    def post(self, request):

        try:
            tenant = TenantService.get_current_tenant(request)
            serializer = ReceivableInvoiceCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            invoice = ReceivableService.create_invoice(
                tenant=tenant,
                user=request.user,
                customer_id=serializer.validated_data["customer_id"],
                invoice_number=serializer.validated_data["invoice_number"],
                invoice_date=serializer.validated_data["invoice_date"],
                due_date=serializer.validated_data["due_date"],
                notes=serializer.validated_data.get("notes", ""),
                items=serializer.validated_data["items"],
                tax_id=serializer.validated_data.get("tax_id"),
            )

            output = ReceivableInvoiceSerializer(invoice)

            return Response(output.data, status=status.HTTP_201_CREATED)

        except Exception as e:

            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class ReceivableInvoiceDetailAPIView(APIView):

    def get(self, request, invoice_id):

        tenant = TenantService.get_current_tenant(request)
        try:

            invoice = ReceivableInvoice.objects.get(
                id=invoice_id, tenant=tenant
            )

            data = ReceivableInvoiceSerializer(invoice).data

            return Response(data)

        except ReceivableInvoice.DoesNotExist:

            return Response(
                {"error": "Invoice not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


class ReceivableInvoicePostAPIView(APIView):

    def post(self, request, invoice_id):

        tenant = TenantService.get_current_tenant(request)

        invoice = get_object_or_404(
            ReceivableInvoice,
            id=invoice_id,
            tenant=tenant,
        )

        try:

            invoice = ReceivableService.post_invoice(
                invoice=invoice,
                user=request.user,
            )

            data = ReceivableInvoiceSerializer(invoice).data

            return Response(data)

        except Exception as e:

            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class OutstandingInvoiceListAPIView(APIView):

    def get(self, request):

        tenant = TenantService.get_current_tenant(request)

        qs = (
            ReceivableInvoice.objects.filter(
                tenant=tenant, status="posted", balance_due__gt=0
            )
            .select_related("customer")
            .order_by("-invoice_date")
        )

        data = []

        for obj in qs:

            data.append(
                {
                    "id": str(obj.id),
                    "customer_id": str(obj.customer.id),
                    "invoice_number": obj.invoice_number,
                    "customer_name": obj.customer.name,
                    "total_amount": obj.total_amount,
                    "paid_amount": obj.paid_amount,
                    "balance_due": obj.balance_due,
                }
            )

        return Response(data)
