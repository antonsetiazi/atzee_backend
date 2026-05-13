# core/activity/events/finance_events.py

"""
Finance activity event definitions.

Provides grouped access to finance events.
"""

from core.activity.constants.events import (
    FINANCE_FIXED_ASSET_ACTIVATED,
    FINANCE_FIXED_ASSET_CREATED,
    FINANCE_FIXED_ASSET_DELETED,
    FINANCE_FIXED_ASSET_DEPRECIATED,
    FINANCE_FIXED_ASSET_DEPRECIATION_RUN,
    FINANCE_FIXED_ASSET_DISPOSED,
    FINANCE_FIXED_ASSET_UPDATED,
    FINANCE_INVOICE_APPROVED,
    FINANCE_INVOICE_CREATED,
    FINANCE_INVOICE_PAID,
    FINANCE_PAYMENT_CREATED,
)


class FinanceEvents:
    """
    Grouped finance activity events.
    """

    # ========================================================
    # FIXED ASSET
    # ========================================================
    FIXED_ASSET_CREATED = FINANCE_FIXED_ASSET_CREATED
    FIXED_ASSET_UPDATED = FINANCE_FIXED_ASSET_UPDATED
    FIXED_ASSET_DELETED = FINANCE_FIXED_ASSET_DELETED
    FIXED_ASSET_DEPRECIATED = FINANCE_FIXED_ASSET_DEPRECIATED
    FIXED_ASSET_DEPRECIATION_RUN = FINANCE_FIXED_ASSET_DEPRECIATION_RUN
    FIXED_ASSET_ACTIVATED = FINANCE_FIXED_ASSET_ACTIVATED
    FIXED_ASSET_DISPOSED = FINANCE_FIXED_ASSET_DISPOSED

    # ========================================================
    # INVOICE
    # ========================================================
    INVOICE_CREATED = FINANCE_INVOICE_CREATED
    INVOICE_APPROVED = FINANCE_INVOICE_APPROVED
    INVOICE_PAID = FINANCE_INVOICE_PAID

    # ========================================================
    # PAYMENT
    # ========================================================
    PAYMENT_CREATED = FINANCE_PAYMENT_CREATED
