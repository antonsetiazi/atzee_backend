# core/ui/schema/block/availability.py

from dataclasses import dataclass, field
from typing import List, Literal, Dict, Optional


@dataclass(frozen=True)
class AvailabilityBlock:
    type: Literal["availability"] = "availability"
    title: Optional[str] = None
    description: Optional[str] = None
    data_source: str = ""
    query_params: Dict[str, str] = field(default_factory=dict)
    mode: Literal["select", "view"] = "select"
    bind_to_field: str = "scheduled_at"
    with_time: bool = True
    height: int = 600
    permissions: Optional[List[str]] = None

