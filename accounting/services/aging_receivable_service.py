# accounting/services/aging_receivable_service.py

from decimal import Decimal
from datetime import date

from accounting.models import (
    ReceivableInvoice
)


class AgingReceivableService:

    @staticmethod
    def generate(tenant):

        today = date.today()

        invoices = ReceivableInvoice.objects.filter(
            tenant=tenant
        ).exclude(
            status__in=["paid", "cancelled"]
        )

        results = []

        summary = {
            "current": Decimal("0"),
            "days_1_30": Decimal("0"),
            "days_31_60": Decimal("0"),
            "days_61_90": Decimal("0"),
            "days_90_plus": Decimal("0"),
            "total": Decimal("0"),
        }

        for invoice in invoices:

            overdue_days = (
                today - invoice.due_date
            ).days

            balance = invoice.balance_due

            bucket = "current"

            if overdue_days <= 0:
                bucket = "current"

            elif overdue_days <= 30:
                bucket = "days_1_30"

            elif overdue_days <= 60:
                bucket = "days_31_60"

            elif overdue_days <= 90:
                bucket = "days_61_90"

            else:
                bucket = "days_90_plus"

            summary[bucket] += balance
            summary["total"] += balance

            results.append({
                "invoice_id": str(invoice.id),

                "invoice_number": invoice.invoice_number,

                "customer_id": str(invoice.customer.id),

                "customer_name": invoice.customer.name,

                "invoice_date": invoice.invoice_date,

                "due_date": invoice.due_date,

                "overdue_days": max(overdue_days, 0),

                "balance_due": balance,

                "bucket": bucket,
            })

        return {
            "summary": summary,
            "items": results,
        }