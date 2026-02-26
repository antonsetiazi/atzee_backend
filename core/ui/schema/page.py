# core/ui/schema/page.py

from dataclasses import dataclass
from typing import Literal, List, Optional, Union


from .block import (
    FormBlock, 
    TableBlock, 
    WorkflowBlock, 
    FileBlock, 
    TagBlock, 
    StatBlock, 
    ChartBlock, 
    TextBlock,
    ContainerBlock,
    ShortcutBlock,
    BannerBlock,
    AvailabilityBlock,
)

PageBlock = Union[
    FormBlock, 
    TableBlock, 
    WorkflowBlock, 
    FileBlock, 
    TagBlock, 
    StatBlock, 
    ChartBlock, 
    TextBlock,
    ContainerBlock,
    ShortcutBlock,
    BannerBlock,
    AvailabilityBlock,
]

HTTPMethod = Literal["GET", "POST", "PATCH", "DELETE"]

@dataclass(frozen=True)
class Page:
    key: str
    entity: str
    domain: str
    title: str
    path: str
    permissions: List[str]
    blocks: List[PageBlock]
    description: Optional[str] = None
    data_source: str = None
    method: HTTPMethod = "POST"
    accept_context: bool = True
    payload_from_context: Optional[dict] = None