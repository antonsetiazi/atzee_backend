# core/ui/schema/block/list.py

from dataclasses import dataclass, field
from typing import List, Literal, Dict, Optional

ListSelectableType = Literal["none", "single", "multiple"]

@dataclass(frozen=True)
class ListItemField:
    key: str
    label: Optional[str] = None
    format: Optional[str] = None

@dataclass(frozen=True)
class ListBlock:
    type: Literal["list"] = "list"
    title: Optional[str] = None
    description: Optional[str] = None
    data_source: str = ""
    query: Dict[str, object] = field(default_factory=dict)
    selectable: ListSelectableType = "none"
    bind_to_field: Optional[str] = None
    value_key: str = "id"
    fields: List[ListItemField] = field(default_factory=list)
    permissions: Optional[List[str]] = None