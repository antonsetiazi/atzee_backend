# accounting/services/receivable_payment_service.py

from decimal import Decimal
from django.db import transaction

from business.customers.models import Customer

from accounting.models import (
    ReceivablePayment,
    ReceivableAllocation,
    ReceivableInvoice,
)

from accounting.services.auto_journal_service import (
    AutoJournalService
)


class ReceivablePaymentService:

    @staticmethod
    @transaction.atomic
    def create_payment(
        *,
        tenant,
        user,
        customer_id,
        payment_number,
        payment_date,
        amount,
        payment_method,
        allocations=[],
        reference="",
        notes=""
    ):

        customer = Customer.objects.get(
            id=customer_id,
            tenant=tenant
        )

        payment = ReceivablePayment.objects.create(
            tenant=tenant,
            customer=customer,
            payment_number=payment_number,
            payment_date=payment_date,
            amount=amount,
            payment_method=payment_method,
            reference=reference,
            notes=notes,
            created_by=user,
        )

        total_allocated = Decimal("0")

        for item in allocations:

            invoice = ReceivableInvoice.objects.get(
                id=item["invoice_id"],
                tenant=tenant
            )

            allocated_amount = Decimal(
                item["allocated_amount"]
            )

            if allocated_amount <= 0:
                raise ValueError(
                    "Allocated amount must be > 0"
                )

            if allocated_amount > invoice.balance_due:
                raise ValueError(
                    f"Allocation exceeds invoice balance: "
                    f"{invoice.invoice_number}"
                )

            ReceivableAllocation.objects.create(
                tenant=tenant,
                payment=payment,
                invoice=invoice,
                allocated_amount=allocated_amount,
                created_by=user,
            )

            invoice.paid_amount += allocated_amount

            invoice.refresh_payment_status()

            total_allocated += allocated_amount

        if total_allocated != Decimal(amount):
            raise ValueError(
                "Allocated amount must equal payment amount"
            )

        # AUTO JOURNAL
        AutoJournalService.create_from_transaction(
            tenant=tenant,
            user=user,
            transaction_type="payment_in",
            reference=payment.payment_number,
            date=payment.payment_date,
            payload={
                "total_amount": payment.amount
            }
        )

        return payment