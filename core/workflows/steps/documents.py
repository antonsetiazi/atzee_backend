# core/workflows/steps/documents.py

from core.workflows.steps.base import WorkflowStep

class CreateInvoiceStep(WorkflowStep):
    name = "documents.create_invoice"

    def execute(self, context):
        trx = context.transaction
        context.log(f"Invoice created for {trx.reference}")
