# core/ui/schema/block/tag.py

from dataclasses import dataclass
from typing import List, Literal, Optional


@dataclass(frozen=True)
class TagBlock:
    type: Literal["tags"] = "tags"
    title: Optional[str] = "Tags"
    description: Optional[str] = None
    entity_type: str = ""          # contoh: "customer"
    entity_id_from: str = "id"     # ambil dari response atau route
    allow_create: bool = True      # boleh buat tag baru
    allow_attach: bool = True      # boleh attach tag
    allow_detach: bool = True      # boleh detach tag
    multiple: bool = True
    permissions: Optional[List[str]] = None
