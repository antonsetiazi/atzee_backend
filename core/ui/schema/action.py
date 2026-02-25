# core/ui/schema/action.py

from dataclasses import dataclass
from typing import Literal, Optional, TypedDict, Dict, Any

ActionType = Literal["submit", "redirect", "navigate", "delete"]
Affects = Literal["session_user", "session_settings", "permissions", "config", "reload"]

class ConfirmConfig(TypedDict, total=False):
    title: str
    message: str
    level: Literal["info", "warning", "danger"]


@dataclass(frozen=True)
class Action:
    type: ActionType
    label: str
    key: str = None
    to: Optional[str] = None
    permission: Optional[str] = None
    icon: Optional[str] = None

    # NEW: condition to show/enable action
    when: Optional[Dict[str, Any]] = None

    # delete / destructive confirmation
    confirm: Optional[ConfirmConfig] = None
    
    # delete endpoint
    endpoint: Optional[str] = None
    affects: Optional[Affects] = None

    success_title: Optional[str] = None
    success_message: Optional[str] = None