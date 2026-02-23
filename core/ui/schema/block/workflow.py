# core/ui/schema/block/workflow.py

from dataclasses import dataclass
from typing import List, Literal, Optional
from ..action import Action


@dataclass(frozen=True)
class WorkflowStatus:
    key: str
    label: str
    color: Optional[str] = None   # gray | blue | green | red | yellow


@dataclass(frozen=True)
class WorkflowBlock:
    status: WorkflowStatus
    actions: List[Action]
    type: Literal["workflow"] = "workflow"
