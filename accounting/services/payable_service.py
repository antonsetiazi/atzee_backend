# accounting/services/payable_service.py

from decimal import Decimal
from django.db import transaction

from business.partners.models import Partner

from accounting.models import (
    PayableInvoice,
    PayableInvoiceItem,
)

from accounting.services.auto_journal_service import (
    AutoJournalService
)


class PayableService:

    @staticmethod
    @transaction.atomic
    def create_invoice(
        *,
        tenant,
        user,
        partner_id,
        invoice_number,
        invoice_date,
        due_date,
        items=[],
        notes=""
    ):

        partner = Partner.objects.get(
            id=partner_id,
            tenant=tenant
        )

        subtotal = Decimal("0")

        for item in items:

            qty = Decimal(item["qty"])

            unit_price = Decimal(
                item["unit_price"]
            )

            subtotal += qty * unit_price

        invoice = PayableInvoice.objects.create(
            tenant=tenant,
            partner=partner,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            due_date=due_date,
            notes=notes,
            subtotal=subtotal,
            total_amount=subtotal,
            balance_due=subtotal,
            status="posted",
            created_by=user,
        )

        for item in items:

            PayableInvoiceItem.objects.create(
                tenant=tenant,
                invoice=invoice,
                description=item["description"],
                qty=item["qty"],
                unit_price=item["unit_price"],
                created_by=user,
            )

        # AUTO JOURNAL
        AutoJournalService.create_from_transaction(
            tenant=tenant,
            user=user,
            transaction_type="purchase_invoice",
            reference=invoice.invoice_number,
            date=invoice.invoice_date,
            payload={
                "total_amount": invoice.total_amount
            }
        )

        return invoice