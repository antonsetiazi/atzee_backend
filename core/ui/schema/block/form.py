# core/ui/schema/block/form.py

from dataclasses import dataclass, field
from typing import List, Literal, Optional
from ..field import Field
from ..action import Action


HTTPMethod = Literal["GET", "POST", "PATCH", "DELETE"]
FormMode = Literal["create", "edit", "view", "filter"]
Affects = Literal["session_user", "session_settings", "permissions", "config"]


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
    affects: Optional[Affects] = None
    refresh_cache: Optional[List[str]] = None
