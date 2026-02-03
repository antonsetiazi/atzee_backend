# core/workflows/steps/__init__.py

from core.workflows.steps.documents import CreateInvoiceStep
from core.workflows.steps.accounting import PostSalesJournalStep
from core.workflows.steps.payments import CreateCashPaymentStep 
from core.workflows.steps.inventory import ReserveStockStep


STEP_MAP = {
    CreateInvoiceStep.name: CreateInvoiceStep(),
    PostSalesJournalStep.name: PostSalesJournalStep(),
    CreateCashPaymentStep.name: CreateCashPaymentStep(),
    ReserveStockStep.name: ReserveStockStep(),
}
