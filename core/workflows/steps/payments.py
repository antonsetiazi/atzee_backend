# core/workflows/steps/payments.py

from core.workflows.steps.base import WorkflowStep
from core.workflows.context import WorkflowContext


class CreateCashPaymentStep(WorkflowStep):
    """
    Create cash payment record for transaction.
    (Placeholder – real payment logic can be added later)
    """

    name = "payments.create_cash"

    def execute(self, context: WorkflowContext) -> None:
        trx = context.transaction

        # Guard: only for sales
        if trx.transaction_type != "SALES":
            return

        # For now: no DB mutation, only domain hook
        # Future:
        # - create Payment model
        # - link to transaction
        # - mark as PAID / PARTIAL
        return
