# core/ui/schema/block/info.py

from dataclasses import dataclass
from typing import Dict, Optional, Any

@dataclass(frozen=True)
class InfoBlock:
    key: str
    title: str
    value: Any
    type: str = "info"
    suffix: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None  # currency, format, suffix
