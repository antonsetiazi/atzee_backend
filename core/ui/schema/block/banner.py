# core/ui/schema/block/banner.py

from dataclasses import dataclass
from typing import Literal, Optional


WidgetSize = Literal["sm", "md", "lg"]

@dataclass(frozen=True)
class BannerBlock:
    type: Literal["banner"] = "banner"
    title: Optional[str] = None
    description: Optional[str] = None
    data_source: str = ""
    size: WidgetSize = "lg"
    