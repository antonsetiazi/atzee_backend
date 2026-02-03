# core/workflows/engine.py

import yaml
from pathlib import Path

from core.workflows.context import WorkflowContext
from core.workflows.registry import workflow_registry
from core.workflows.steps import STEP_MAP

class WorkflowEngine:
    """
    Execute workflow based on definition.
    """

    @staticmethod
    def run(*, event: str, context: WorkflowContext):
        workflow = workflow_registry.get_workflow(
            event=event,
            transaction=context.transaction,
        )

        if not workflow:
            return

        for step_name in workflow["steps"]:
            step = STEP_MAP[step_name]
            step.execute(context)
