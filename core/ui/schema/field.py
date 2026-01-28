# core/ui/schema/field.py

from dataclasses import dataclass
from typing import Literal, Optional, List, Any


FieldType = Literal["text", "email", "textarea", "hidden", "select"]


@dataclass(frozen=True)
class Field:
    key: str
    label: str
    type: FieldType
    required: bool = False
    options: Optional[List[dict[str, Any]]] = None