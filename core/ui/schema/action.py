# core/ui/schema/action.py

from dataclasses import dataclass
from typing import Literal, Optional, TypedDict

ActionType = Literal["submit", "redirect", "navigate", "delete"]


class ConfirmConfig(TypedDict, total=False):
    title: str
    message: str
    level: Literal["info", "warning", "danger"]


@dataclass(frozen=True)
class Action:
    type: ActionType
    label: str
    to: Optional[str] = None
    permission: Optional[str] = None

    # delete / destructive confirmation
    confirm: Optional[ConfirmConfig] = None
    
    # delete endpoint
    endpoint: Optional[str] = None