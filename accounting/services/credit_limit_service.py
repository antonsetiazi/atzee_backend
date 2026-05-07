# accounting/services/credit_limit_service.py

from decimal import Decimal

from accounting.models import (
    ReceivableInvoice,
    AccountingConfig,
)


class CreditLimitService:

    @staticmethod
    def get_customer_outstanding(
        *,
        tenant,
        customer
    ):

        invoices = ReceivableInvoice.objects.filter(
            tenant=tenant,
            customer=customer,
        ).exclude(
            status__in=["paid", "cancelled"]
        )

        total = Decimal("0")

        for inv in invoices:
            total += inv.balance_due

        return total


    @staticmethod
    def validate_new_invoice(
        *,
        tenant,
        customer,
        invoice_amount,
    ):

        config = AccountingConfig.objects.filter(
            tenant=tenant
        ).first()

        # default behavior
        if not config:
            return

        if not config.enforce_credit_limit:
            return

        outstanding = (
            CreditLimitService.get_customer_outstanding(
                tenant=tenant,
                customer=customer
            )
        )

        projected = (
            outstanding +
            Decimal(invoice_amount)
        )

        credit_limit = customer.credit_limit or 0

        if projected > credit_limit:

            if not config.allow_over_credit:

                raise ValueError(
                    f"Customer exceeds credit limit. "
                    f"Limit={credit_limit} "
                    f"Outstanding={outstanding} "
                    f"Projected={projected}"
                )

        return {
            "credit_limit": credit_limit,
            "outstanding": outstanding,
            "projected": projected,
        }