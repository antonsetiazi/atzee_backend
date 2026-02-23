# core/ui/schema/block/container.py

from dataclasses import dataclass, field
from typing import List, Literal, Optional, Any


LayoutDirection = Literal["row", "column"]
LayoutJustify = Literal["start", "center", "between", "around"]
LayoutAlign = Literal["start", "center", "stretch"]


@dataclass(frozen=True)
class ContainerBlock:
    type: Literal["container"] = "container"
    
    # layout
    direction: LayoutDirection = "row"
    wrap: bool = True
    gap: int = 16
    justify: LayoutJustify = "start"
    align: LayoutAlign = "stretch"
    columns: Optional[int] = None  # kalau mau grid mode
    
    # tambahan
    key: Optional[str] = None
    background_color: Optional[str] = None  # misal "bg-white", "bg-gray-50"
   
    # isi
    blocks: List[Any] = field(default_factory=list)
