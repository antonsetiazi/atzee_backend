# core/ui/schema/block.py

from dataclasses import dataclass, field
from typing import List, Literal, Optional

from .field import Field
from .action import Action
from .base import HTTPMethod


BlockType = Literal["form", "table", "workflow"]
searchModeType = Literal["server", "client"]
FormMode = Literal["create", "edit", "view"]

@dataclass(frozen=True)
class FormRedirect:
    page: str                 # page key, contoh: sales.direct.detail
    param: str = "id"          # field dari response


@dataclass(frozen=True)
class FormBlock:
    type: Literal["form"] = "form"

    mode: FormMode = "create"   # 🔥 DEFAULT

    submit_to: str = ""
    method: HTTPMethod = "POST"

    title: Optional[str] = None
    description: Optional[str] = None

    fields: List[Field] = field(default_factory=list)
    actions: List[Action] = field(default_factory=list)

    redirect_to: Optional[FormRedirect] = None

    
@dataclass(frozen=True)
class TableColumn:
    key: str
    label: str


@dataclass(frozen=True)
class TableBlock:
    type: Literal["table"] = "table"
    
    title: Optional[str] = None
    description: Optional[str] = None

    data_source: str = ""
    search_mode: searchModeType = "client"
    
    columns: List[TableColumn] = field(default_factory=list)
    
    actions: List[Action] = field(default_factory=list)
    top_actions: List[Action] = field(default_factory=list)

    detail_as_state: bool = False
    

@dataclass(frozen=True)
class WorkflowStatus:
    key: str
    label: str
    color: Optional[str] = None   # gray | blue | green | red | yellow


@dataclass(frozen=True)
class WorkflowBlock:
    status: WorkflowStatus
    actions: List[Action]
    type: Literal["workflow"] = "workflow"