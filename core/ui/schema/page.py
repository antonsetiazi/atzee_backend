# core/ui/schema/page.py

from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional, Union

from .action import Action
from .block import (
    AvailabilityBlock,
    BannerBlock,
    CategorySliderBlock,
    ChartBlock,
    ContainerBlock,
    FileBlock,
    FormBlock,
    ListingSectionBlock,
    ShortcutBlock,
    StatBlock,
    TableBlock,
    TagBlock,
    TextBlock,
    WorkflowBlock,
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
    ListingSectionBlock,
    ContainerBlock,
    ShortcutBlock,
    BannerBlock,
    AvailabilityBlock,
    CategorySliderBlock,
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
    subtitle: Optional[str] = None
    description: Optional[str] = None
    data_source: str = None
    method: HTTPMethod = "POST"
    accept_context: bool = True
    payload_from_context: Optional[dict] = None
    meta: Optional[Dict[str, Any]] = None
    actions: Optional[List[Action]] = None
