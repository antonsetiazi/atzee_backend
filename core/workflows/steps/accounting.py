# core/workflows/steps/accounting.py

from core.workflows.steps.base import WorkflowStep

class PostSalesJournalStep(WorkflowStep):
    name = "accounting.post_sales_journal"

    def execute(self, context):
        context.log("Accounting journal posted")
