# accounting/api/receivables_dashboard/views.py

from decimal import Decimal

from django.db.models import Sum
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import (
    ReceivableInvoice,
    ReceivablePayment,
)
from core.tenants.services import TenantService


class ReceivableDashboardAPIView(APIView):

    def get(self, request):

        tenant = TenantService.get_current_tenant(request)

        today = timezone.now().date()

        invoices = ReceivableInvoice.objects.filter(tenant=tenant)

        payments = ReceivablePayment.objects.filter(tenant=tenant)

        # =====================================
        # TOTAL RECEIVABLE
        # =====================================

        total_receivable = invoices.aggregate(total=Sum("balance_due"))[
            "total"
        ] or Decimal("0")

        # =====================================
        # OVERDUE
        # =====================================

        overdue_qs = invoices.filter(
            due_date__lt=today,
            balance_due__gt=0,
        )

        overdue_amount = overdue_qs.aggregate(total=Sum("balance_due"))[
            "total"
        ] or Decimal("0")

        overdue_count = overdue_qs.count()

        # =====================================
        # PAID THIS MONTH
        # =====================================

        paid_this_month = payments.filter(
            payment_date__year=today.year,
            payment_date__month=today.month,
        ).aggregate(total=Sum("amount"))["total"] or Decimal("0")

        # =====================================
        # DRAFT INVOICES
        # =====================================

        draft_count = invoices.filter(status="draft").count()

        # =====================================
        # RECENT INVOICES
        # =====================================

        recent_invoices = invoices.order_by(
            "-invoice_date",
            "-created_at",
        )[:5]

        recent_invoices_data = [
            {
                "id": str(item.id),
                "invoice_number": item.invoice_number,
                "customer_name": item.customer.name,
                "status": item.status,
                "total_amount": item.total_amount,
            }
            for item in recent_invoices
        ]

        # =====================================
        # RECENT PAYMENTS
        # =====================================

        recent_payments = payments.order_by(
            "-payment_date",
            "-created_at",
        )[:5]

        recent_payments_data = [
            {
                "id": str(item.id),
                "payment_number": item.payment_number,
                "customer_name": item.customer.name,
                "amount": item.amount,
            }
            for item in recent_payments
        ]

        return Response(
            {
                "summary": {
                    "total_receivable": total_receivable,
                    "overdue_amount": overdue_amount,
                    "overdue_count": overdue_count,
                    "paid_this_month": paid_this_month,
                    "draft_count": draft_count,
                },
                "recent_invoices": (recent_invoices_data),
                "recent_payments": (recent_payments_data),
            }
        )
