# core/ui/schema/block/stat.py

from dataclasses import dataclass
from typing import Literal, Dict, Optional, Any


WidgetSize = Literal["sm", "md", "lg"]

@dataclass(frozen=True)
class StatBlock:
    key: str
    title: str
    value: Any
    type: Literal["stat"] = "stat"
    size: WidgetSize = "md"
    suffix: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None  # currency, format, suffix
