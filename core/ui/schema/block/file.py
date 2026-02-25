# core/ui/schema/block/file.py

from dataclasses import dataclass
from typing import List, Literal, Optional

Affects = Literal["session_user", "session_settings", "permissions", "config", "reload"]

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
    affects: Optional[Affects] = None
