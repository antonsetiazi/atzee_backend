# core/workflows/steps/base.py

from abc import ABC, abstractmethod

class WorkflowStep(ABC):
    """
    Base workflow step.
    """

    name: str

    @abstractmethod
    def execute(self, context):
        """
        Execute step logic.
        """
        pass
