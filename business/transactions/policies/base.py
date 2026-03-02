# business/transactions/policies/base.py

from django.core.exceptions import ValidationError
from business.transactions.models.enums import (
    TransactionType,
    TransactionSubType,
)


class BaseTransactionPolicy:
    """
    Default business-level invariant rules.
    """

    def validate(self, *, transaction_type, subtype, customer, partner, items):

        # Generic invariant (berlaku untuk semua)
        if not items:
            raise ValidationError(
                "Transaction must contain at least one item."
            )

        # Dispatch per type
        handler = self._get_handler(transaction_type)
        if handler:
            handler(
                subtype=subtype,
                customer=customer,
                partner=partner,
                items=items,
            )

    # =========================
    # Type dispatcher
    # =========================

    def _get_handler(self, transaction_type):
        return {
            TransactionType.SALES: self._validate_sales,
            TransactionType.PURCHASE: self._validate_purchase,
        }.get(transaction_type)

    # =========================
    # Per-type rules
    # =========================

    def _validate_sales(self, *, subtype, customer, **kwargs):

        if subtype in [
            TransactionSubType.ORDER,
            TransactionSubType.SERVICE,
            TransactionSubType.CONSIGNMENT,
        ]:
            if not customer:
                raise ValidationError(
                    "This sales subtype requires customer."
                )

    def _validate_purchase(self, *, partner, **kwargs):

        if not partner:
            raise ValidationError(
                "Purchase transaction requires partner."
            )