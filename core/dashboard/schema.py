# core/dashboard/schema.py

from dataclasses import dataclass, field
from typing import Literal, Optional, Dict, Any

WidgetType = Literal[
    "stat",
    "table",
    "chart",
    "text",
]

WidgetSize = Literal["sm", "md", "lg"]


@dataclass
class DashboardWidget:
    key: str
    type: WidgetType
    title: str
    source: Dict[str, Any]
    """
    contoh:
    {
        "service": "dashboard.total_users",
        "params": {}
    }
    """

    size: WidgetSize = "md"
    permission: Optional[str] = None
    meta: Dict[str, Any] = field(default_factory=dict)
