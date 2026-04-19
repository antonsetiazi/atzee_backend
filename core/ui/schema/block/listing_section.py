# core/ui/schema/block/listing_section.py

from dataclasses import dataclass
from typing import Optional, Literal

ListingSectionType = Literal[
    "popular_services",
    "nearby_services",
    "new_services",
    "recommended_services",
    "top_rated_services",
    "cheap_services",
]

@dataclass(frozen=True)
class ListingSectionBlock:
    type: str = "listing_section"

    title: str = ""
    section_type: ListingSectionType = "popular_services"

    limit: int = 4
    subtitle: Optional[str] = None
    view_all_to: Optional[str] = "/services"