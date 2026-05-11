# accounting/services/payable_payment_service.py

from decimal import Decimal

from django.db import transaction

from accounting.models import (
    PayableAllocation,
    PayableInvoice,
    PayablePayment,
)
from accounting.services.auto_journal_service import AutoJournalService
from business.partners.models import Partner


class PayablePaymentService:

    # =========================================================
    # CREATE PAYMENT (DRAFT ONLY - NO ACCOUNTING IMPACT)
    # =========================================================
    @staticmethod
    @transaction.atomic
    def create_payment(
        *,
        tenant,
        user,
        partner_id,
        payment_number,
        payment_date,
        amount,
        payment_method,
        allocations=None,
        reference="",
        notes="",
    ):

        if allocations is None:
            allocations = []

        partner = Partner.objects.get(id=partner_id, tenant=tenant)

        amount = Decimal(str(amount))

        payment = PayablePayment.objects.create(
            tenant=tenant,
            partner=partner,
            payment_number=payment_number,
            payment_date=payment_date,
            amount=amount,
            payment_method=payment_method,
            reference=reference,
            notes=notes,
            status="draft",
            created_by=user,
        )

        total_allocated = Decimal("0")

        for item in allocations:
            invoice = PayableInvoice.objects.get(
                id=item["invoice_id"], tenant=tenant
            )

            allocated_amount = Decimal(item["allocated_amount"])

            if allocated_amount <= 0:
                raise ValueError("Allocated amount must be > 0")

            if allocated_amount > invoice.balance_due:
                raise ValueError(
                    f"Allocation exceeds invoice balance: "
                    f"{invoice.invoice_number}"
                )

            PayableAllocation.objects.create(
                tenant=tenant,
                payment=payment,
                invoice=invoice,
                allocated_amount=allocated_amount,
                created_by=user,
            )

            total_allocated += allocated_amount

            # invoice.paid_amount += allocated_amount

            # invoice.refresh_payment_status()

        if total_allocated != Decimal(amount):
            raise ValueError("Allocated amount must equal payment amount")

        return payment

    # =========================================================
    # POST PAYMENT (REAL ACCOUNTING IMPACT)
    # =========================================================
    @staticmethod
    @transaction.atomic
    def post_payment(*, payment, user):

        # =========================
        # VALIDATION
        # =========================
        if payment.status != "draft":
            raise ValueError("Only draft payments can be posted")

        # =========================
        # CREATE JOURNAL ENTRY
        # =========================
        AutoJournalService.create_from_transaction(
            tenant=payment.tenant,
            user=user,
            transaction_type="payment_out",
            reference=payment.payment_number,
            date=payment.payment_date,
            payload={
                "total_amount": payment.amount,
            },
        )

        # =========================
        # UPDATE INVOICE BALANCE (REAL IMPACT)
        # =========================
        allocations = PayableAllocation.objects.filter(
            payment=payment
        ).select_related("invoice")

        for alloc in allocations:
            invoice = alloc.invoice
            invoice.paid_amount += alloc.allocated_amount
            invoice.refresh_payment_status()
            invoice.save()

        # =========================
        # LOCK PAYMENT
        # =========================
        payment.status = "posted"
        payment.save()

        return payment
