# core/ui/schema/block.py

from dataclasses import dataclass, field
from typing import List, Literal, Dict, Optional

from .field import Field
from .action import Action
from .base import HTTPMethod


BlockType = Literal["form", "table", "workflow", "files"]
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
    type: Optional[str] = None

    # UI metadata (optional)
    align: Optional[str] = None        # "left" | "right" | "center"
    width: Optional[int] = None        # px
    format: Optional[str] = None       # "currency", "date", etc
    

@dataclass(frozen=True)
class TableBlock:
    type: Literal["table"] = "table"
    
    title: Optional[str] = None
    description: Optional[str] = None

    data_source: str = ""
    
    query: Dict[str, object] = field(default_factory=dict)

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


@dataclass(frozen=True)
class FileBlock:
    type: Literal["files"] = "files"

    title: Optional[str] = "Attachments"
    description: Optional[str] = None

    entity_type: str = ""        # "customer"
    entity_id_from: str = "id"   # ambil dari form response / route

    multiple: bool = True
    accept: Optional[str] = None   # "image/*,.pdf"

    permissions: Optional[List[str]] = None    