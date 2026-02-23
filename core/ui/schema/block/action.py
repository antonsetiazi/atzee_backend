# core/ui/schema/block/action.py

from dataclasses import dataclass, field
from typing import List, Literal, Optional
from ..action import Action


LayoutDirection = Literal["row", "column"]
LayoutJustify = Literal["start", "center", "between", "around"]
LayoutAlign = Literal["start", "center", "stretch"]

@dataclass(frozen=True)
class ActionBlock:
    type: Literal["action"] = "action"
    title: Optional[str] = None
    description: Optional[str] = None
    actions: List[Action] = field(default_factory=list)
    direction: LayoutDirection = "row"
    gap: int = 12
    justify: LayoutJustify = "start"
    align: LayoutAlign = "center"
    wrap: bool = True

