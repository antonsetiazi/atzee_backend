# core/ui/schema/page.py

from dataclasses import dataclass
from typing import List, Optional

from .block import FormBlock


@dataclass(frozen=True)
class Page:
    key: str
    entity: str
    domain: str
    title: str
    permissions: List[str]
    blocks: List[FormBlock]
    description: Optional[str] = None