# core/ui/schema/block/table.py

from dataclasses import dataclass, field
from typing import List, Literal, Dict, Optional
from ..action import Action


searchModeType = Literal["server", "client"]
    
    
@dataclass(frozen=True)
class TableColumn:
    key: str
    label: str
    type: Optional[str] = None
    priority: Optional[int] = None
    # UI metadata (optional)
    align: Optional[str] = None        # "left" | "right" | "center"
    width: Optional[int] = None        # px
    format: Optional[str] = None       # "currency", "date", etc
    

@dataclass(frozen=True)
class TableBlock:
    type: Literal["table"] = "table"
    title: Optional[str] = None
    description: Optional[str] = None
    data_key: Optional[str] = None
    data_source: str = ""
    query: Dict[str, object] = field(default_factory=dict)
    search_mode: searchModeType = "client"
    columns: List[TableColumn] = field(default_factory=list)  
    actions: List[Action] = field(default_factory=list)
    top_actions: List[Action] = field(default_factory=list)
    detail_as_state: bool = False
    