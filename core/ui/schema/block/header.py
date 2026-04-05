# core/ui/schema/block/header.py

from dataclasses import dataclass
from typing import Optional, Literal


HeaderVariant = Literal["default", "home", "dashboard"]


@dataclass(frozen=True)
class HeaderBlock:
    type: Literal["header"] = "header"

    title: Optional[str] = None
    subtitle: Optional[str] = None

    # 🔥 behavior
    variant: HeaderVariant = "default"

    # 🔥 data binding (optional)
    data_key: Optional[str] = None

    # 🔥 feature flags (future-proof)
    show_search: bool = False
    show_avatar: bool = False
    show_greeting: bool = False