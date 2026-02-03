# core/workflows/registry.py

from core.workflows.loader import load_workflow_definitions


class WorkflowRegistry:
    def __init__(self):
        self._workflows = {}
        self._load_from_definitions()
        print(f"[WorkflowRegistry] loaded {len(self._workflows)} workflows")

    def _load_from_definitions(self):
        """
        Load workflows from YAML definitions at startup.
        """
        for wf in load_workflow_definitions():
            key = (
                wf["event"],
                wf["transaction_type"],
                wf.get("subtype"),
            )
            self._workflows[key] = wf

    def register(self, *, event, transaction_type, subtype, definition):
        """
        Manual registration (still supported).
        """
        key = (event, transaction_type, subtype)
        self._workflows[key] = definition

    def get_workflow(self, *, event, transaction):
        return self._workflows.get(
            (event, transaction.transaction_type, transaction.subtype)
        )


workflow_registry = WorkflowRegistry()

