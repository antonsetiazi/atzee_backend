# core/ui/schema/block/transaction_summary.py

from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class TransactionSummaryBlock:
    """
    Generic transaction summary block.

    Used to preview pricing breakdown before confirmation.
    Can be used for bookings, orders, rentals, subscriptions, etc.
    """

    type: str = "transaction_summary"

    title: Optional[str] = "Ringkasan Transaksi"
    description: Optional[str] = None

    # endpoint to calculate estimate
    data_source: Optional[str] = None

    # bind to form data for live recalculation
    bind_to_form: bool = False

    # optional additional query params
    query_params: Dict[str, Any] = field(default_factory=dict)

    # layout option (vertical / compact / card)
    layout: str = "vertical"

    # show/hide specific sections
    show_items: bool = True
    show_adjustments: bool = True
    show_tax: bool = True
    show_discount: bool = True
    show_grand_total: bool = True