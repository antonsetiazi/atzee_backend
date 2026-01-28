# core/ui/schema/page.py

from dataclasses import dataclass
from typing import List

from .block import FormBlock


@dataclass(frozen=True)
class Page:
    key: str
    entity: str
    title: str
    permissions: List[str]
    blocks: List[FormBlock]