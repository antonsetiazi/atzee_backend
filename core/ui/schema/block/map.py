# core/ui/schema/block/map.py

from dataclasses import dataclass
from typing import List, Literal, Optional


@dataclass(frozen=True)
class MapBlock:
    type: Literal["map"] = "map"
    title: Optional[str] = "Location"
    description: Optional[str] = None
    entity_type: str = ""         # contoh: "customers"
    entity_id_from: str = "id"    # ambil dari response / route
    mode: Literal["view", "select"] = "view"
    multiple: bool = True
    height: int = 400
    permissions: Optional[List[str]] = None
