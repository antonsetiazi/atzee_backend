# core/ui/schema/block/list_view.py

from dataclasses import dataclass, field
from typing import Optional, Literal, Dict, List
from core.ui.schema.action import Action

ListSelectableType = Literal["none", "single", "multiple"]
ListDensityType = Literal["comfortable", "compact"]
ListLayoutType = Literal["standard", "card"]

# 🔥 Universal Field Config
@dataclass(frozen=True)
class ListFieldSchema:
    key: str
    format: Optional[str] = None
    currency: Optional[str] = None
    suffix: Optional[str] = None
    prefix: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    

@dataclass(frozen=True)
class ListTileSchema:
    title: ListFieldSchema
    subtitle: Optional[ListFieldSchema] = None
    description: Optional[ListFieldSchema] = None
    leading: Optional[ListFieldSchema] = None
    trailing: Optional[ListFieldSchema] = None
    status: Optional[ListFieldSchema] = None
    meta: Dict[str, ListFieldSchema] = field(default_factory=dict)
    action: Optional[Action] = None


@dataclass(frozen=True)
class ListViewBlock:
    type: Literal["list_view"] = "list_view"

    title: Optional[str] = None
    description: Optional[str] = None

    # 🔥 BUKAN data_source
    data_key: Optional[str] = None

    layout: ListLayoutType = "standard"
    density: ListDensityType = "comfortable"

    selectable: ListSelectableType = "none"
    bind_to_field: Optional[str] = None
    value_key: str = "id"

    tile: ListTileSchema = field(default_factory=ListTileSchema)
    
    permissions: Optional[List[str]] = None

    empty_title: str = "No data found"
    empty_description: Optional[str] = None