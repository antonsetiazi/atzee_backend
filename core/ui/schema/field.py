# core/ui/schema/field.py

from dataclasses import dataclass
from typing import Literal, Optional, List, Any

FieldType = Literal[
    "text", 
    "email", 
    "textarea", 
    "hidden", 
    "select", 
    "boolean",
]


@dataclass(frozen=True)
class Field:
    key: str
    label: str
    type: FieldType
    required: bool = False
    disabled: bool = False
    options: Optional[List[dict[str, Any]]] = None

    placeholder: Optional[str] = None
    default: Any = None

    # 🔥 OPTIONAL — hanya dipakai oleh field tertentu (select, relation)
    data_source: Optional[str] = None
    value_key: Optional[str] = None
    label_key: Optional[str] = None

    params: Optional[dict[str, Any]] = None
    
    bind: Optional[str] = None
    readonly_when_bound: bool = False