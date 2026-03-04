# core/ui/schema/block/chart.py

from dataclasses import dataclass
from typing import Literal, Dict, Optional, Any


WidgetSize = Literal["sm", "md", "lg"]

@dataclass(frozen=True)
class ChartBlock:
    key: str
    title: str
    value: Any = None
    type: Literal["chart"] = "chart"
    size: WidgetSize = "md"
    meta: Optional[Dict[str, Any]] = None
    data_key: Optional[str] = None
