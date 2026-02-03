# core/workflows/resolver.py

from django.core.exceptions import ValidationError
from core.workflows.loader import load_workflow_definitions


def resolve_workflow(*, event: str, transaction_type: str, subtype: str):
    workflows = load_workflow_definitions()

    for wf in workflows:
        if (
            wf["event"] == event
            and wf["transaction_type"] == transaction_type
            and wf["subtype"] == subtype
        ):
            return wf

    raise ValidationError(
        f"No workflow for event={event}, "
        f"type={transaction_type}, subtype={subtype}"
    )
