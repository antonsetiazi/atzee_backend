# core/ui/schema/block/shortcut.py

from dataclasses import dataclass, field
from typing import List, Literal, Dict, Optional, Any


@dataclass(frozen=True)
class ShortcutItem:
    key: str                   # unique key
    label: str                  # nama menu
    icon: Optional[str] = None  # optional icon
    to: Optional[str] = None    # route / link
    permission: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None  # bisa simpan info tambahan


@dataclass(frozen=True)
class ShortcutBlock:
    type: Literal["shortcut"] = "shortcut"
    title: Optional[str] = None
    description: Optional[str] = None
    items: List[ShortcutItem] = field(default_factory=list)
    scrollable: bool = True  # kalau panjang bisa scroll horizontal
    center: bool = True      # rata tengah

