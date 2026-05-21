# core/ui/schema/header.py

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class HeaderMeta:
    label: str
    value: Optional[str] = None
    color: Optional[str] = None
