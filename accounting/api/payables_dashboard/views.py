# accounting/api/payables_dashboard/views.py

from decimal import Decimal

from django.db.models import Sum
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView

from accounting.models import (
    PayableInvoice,
    PayablePayment,
)
from core.tenants.services import TenantService


class PayablesDashboardAPIView(APIView):

    def get(self, request):

        tenant = TenantService.get_current_tenant(request)

        today = now().date()

        invoices = PayableInvoice.objects.filter(tenant=tenant)

        payments = PayablePayment.objects.filter(tenant=tenant)

        total_payable = invoices.exclude(status="paid").aggregate(
            total=Sum("balance_due")
        ).get("total") or Decimal("0")

        overdue_qs = invoices.filter(due_date__lt=today).exclude(status="paid")

        overdue_amount = overdue_qs.aggregate(total=Sum("balance_due")).get(
            "total"
        ) or Decimal("0")

        overdue_count = overdue_qs.count()

        paid_this_month = payments.filter(
            payment_date__year=today.year,
            payment_date__month=today.month,
        ).aggregate(total=Sum("amount")).get("total") or Decimal("0")

        draft_count = invoices.filter(status="draft").count()

        recent_invoices = invoices.order_by("-invoice_date")[:5]

        recent_payments = payments.order_by("-payment_date")[:5]

        return Response(
            {
                "summary": {
                    "total_payable": total_payable,
                    "overdue_amount": overdue_amount,
                    "overdue_count": overdue_count,
                    "paid_this_month": paid_this_month,
                    "draft_count": draft_count,
                },
                "recent_invoices": [
                    {
                        "id": inv.id,
                        "invoice_number": inv.invoice_number,
                        "partner_name": inv.partner.name,
                        "total_amount": inv.total_amount,
                        "status": inv.status,
                    }
                    for inv in recent_invoices
                ],
                "recent_payments": [
                    {
                        "id": pay.id,
                        "payment_number": pay.payment_number,
                        "partner_name": pay.partner.name,
                        "amount": pay.amount,
                    }
                    for pay in recent_payments
                ],
            }
        )
