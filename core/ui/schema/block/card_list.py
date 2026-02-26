# core/ui/schema/block/card_list.py

from dataclasses import dataclass, field
from typing import List, Literal, Dict, Optional, Any
from core.ui.schema.action import Action

CardSelectableType = Literal["none", "single", "multiple"]
CardLayoutType = Literal["grid", "list"]


@dataclass(frozen=True)
class CardField:
    key: str
    label: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None  # currency, format, suffix


@dataclass(frozen=True)
class CardListBlock:
    type: Literal["card_list"] = "card_list"
    title: Optional[str] = None
    description: Optional[str] = None

    data_key: Optional[str] = None

    data_source: str = ""
    query: Dict[str, object] = field(default_factory=dict)
    value_key: str = "id"   # default ambil id dari response
    label_key: Optional[str] = None
    layout: CardLayoutType = "grid"
    columns: int = 2
    selectable: CardSelectableType = "none"
    bind_to_field: Optional[str] = None
    fields: List[CardField] = field(default_factory=list)
    item_action: Optional[Action] = None
    permissions: Optional[List[str]] = None