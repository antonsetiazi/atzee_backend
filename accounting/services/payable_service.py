# accounting/services/payable_service.py

from decimal import Decimal

from django.db import transaction

from accounting.models import PayableInvoice, PayableInvoiceItem, Tax
from accounting.services.tax_service import TaxService
from business.partners.models import Partner


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
        tax_id=None,
        notes="",
    ):

        partner = Partner.objects.get(id=partner_id, tenant=tenant)

        subtotal = Decimal("0")

        # =========================
        # CALCULATE SUBTOTAL
        # =========================
        for item in items:
            qty = Decimal(item["qty"])
            unit_price = Decimal(item["unit_price"])
            subtotal += qty * unit_price

        # =========================
        # TAX CALCULATION
        # =========================
        tax = None
        tax_amount = Decimal("0")
        grand_total = subtotal

        if tax_id:
            tax = Tax.objects.get(
                id=tax_id,
                tenant=tenant,
            )

            tax_result = TaxService.calculate_tax(
                subtotal=subtotal,
                tax_rate=tax.rate,
            )

            tax_amount = tax_result["tax_amount"]
            grand_total = tax_result["total"]

        # =========================
        # CREATE INVOICE
        # =========================
        invoice = PayableInvoice.objects.create(
            tenant=tenant,
            partner=partner,
            tax=tax,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            due_date=due_date,
            notes=notes,
            subtotal=subtotal,
            tax_amount=tax_amount,
            total_amount=grand_total,
            paid_amount=0,
            balance_due=grand_total,
            status="draft",
            created_by=user,
        )

        # =========================
        # CREATE ITEMS
        # =========================
        for item in items:
            PayableInvoiceItem.objects.create(
                tenant=tenant,
                invoice=invoice,
                description=item["description"],
                qty=item["qty"],
                unit_price=item["unit_price"],
                created_by=user,
            )

        return invoice

    @staticmethod
    @transaction.atomic
    def post_invoice(
        *,
        invoice,
        user,
    ):

        from accounting.services.auto_journal_service import AutoJournalService

        if invoice.status != "draft":
            raise ValueError("Only draft invoices can be posted")

        AutoJournalService.create_from_transaction(
            tenant=invoice.tenant,
            user=user,
            transaction_type="purchase_invoice",
            reference=invoice.invoice_number,
            date=invoice.invoice_date,
            payload={
                "subtotal": invoice.subtotal,
                "tax_amount": invoice.tax_amount,
                "total_amount": invoice.total_amount,
            },
        )

        invoice.status = "posted"

        invoice.save(
            update_fields=[
                "status",
            ]
        )

        return invoice
