# core/workflows/steps/inventory.py

from core.workflows.steps.base import WorkflowStep
from core.workflows.context import WorkflowContext


class ReserveStockStep(WorkflowStep):
    """
    Reserve stock for transaction items.
    """

    name = "inventory.reserve_stock"

    def execute(self, context: WorkflowContext) -> None:
        trx = context.transaction

        # Guard: only sales affect stock
        if trx.transaction_type != "SALES":
            return

        # Future:
        # - check stock availability
        # - create StockReservation records
        # - reduce available stock (soft)
        return
