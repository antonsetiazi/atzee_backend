# core/ui/schema/block.py

from dataclasses import dataclass
from typing import List, Literal, Optional

from .field import Field
from .action import Action
from .base import HTTPMethod


BlockType = Literal["form", "table"]

@dataclass(frozen=True)
class FormBlock:
    type: Literal["form"] = "form"

    submit_to: str = ""
    method: HTTPMethod = "POST"

    title: Optional[str] = None
    description: Optional[str] = None

    fields: List[Field] = None
    actions: List[Action] = None


@dataclass(frozen=True)
class TableColumn:
    key: str
    label: str


@dataclass(frozen=True)
class TableBlock:
    type: Literal["table"] = "table"
    data_source: str = ""
    columns: List[TableColumn] = None
    actions: List[Action] = None
    top_actions: List[Action] = None
