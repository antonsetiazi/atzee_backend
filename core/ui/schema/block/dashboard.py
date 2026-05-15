# core/ui/schema/block/dashboard.py

from dataclasses import dataclass, field
from typing import Any, Dict, Literal, Optional


@dataclass(frozen=True)
class DashboardBlock:
    type: Literal["dashboard"] = "dashboard"

    # Optional UI metadata
    title: Optional[str] = None
    subtitle: Optional[str] = None

    # Optional frontend preset / variant
    variant: Optional[str] = None

    # Optional binding key from pageData
    data_key: Optional[str] = None

    # Extra frontend config
    props: Dict[str, Any] = field(default_factory=dict)
