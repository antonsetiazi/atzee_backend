# core/ui/schema/block/text.py

from dataclasses import dataclass
from typing import Literal, Dict, Optional, Any


WidgetSize = Literal["sm", "md", "lg"]

@dataclass(frozen=True)
class TextBlock:
    key: str
    title: str
    value: str
    type: Literal["text"] = "text"
    size: WidgetSize = "md"
    meta: Optional[Dict[str, Any]] = None
