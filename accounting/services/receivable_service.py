# accounting/services/receivable_service.py

from decimal import Decimal
from django.db import transaction

from business.customers.models import Customer

from accounting.models import (
    ReceivableInvoice,
    ReceivableInvoiceItem
)

from accounting.services.auto_journal_service import (
    AutoJournalService
)

from accounting.services.credit_limit_service import (
    CreditLimitService
)


class ReceivableService:

    @staticmethod
    @transaction.atomic
    def create_invoice(
        *,
        tenant,
        user,
        customer_id,
        invoice_number,
        invoice_date,
        due_date,
        items=[],
        notes=""
    ):

        customer = Customer.objects.get(
            id=customer_id,
            tenant=tenant
        )

        subtotal = Decimal("0")

        for item in items:

            qty = Decimal(item["qty"])

            unit_price = Decimal(
                item["unit_price"]
            )

            subtotal += qty * unit_price


        CreditLimitService.validate_new_invoice(
            tenant=tenant,
            customer=customer,
            invoice_amount=subtotal
        )

        invoice = ReceivableInvoice.objects.create(
            tenant=tenant,
            customer=customer,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            due_date=due_date,
            notes=notes,
            created_by=user
        )

        subtotal = Decimal("0")

        for item in items:

            obj = ReceivableInvoiceItem.objects.create(
                tenant=tenant,
                invoice=invoice,
                description=item["description"],
                qty=item["qty"],
                unit_price=item["unit_price"]
            )

            subtotal += obj.total

        invoice.subtotal = subtotal
        invoice.total_amount = subtotal
        invoice.balance_due = subtotal
        invoice.status = "posted"

        invoice.save()

        # AUTO JOURNAL
        AutoJournalService.create_from_transaction(
            tenant=tenant,
            user=user,
            transaction_type="sales_invoice",
            reference=invoice.invoice_number,
            date=invoice.invoice_date,
            payload={
                "total_amount": invoice.total_amount
            }
        )

        return invoice