# core/ui/schema/page.py

from dataclasses import dataclass
from typing import List, Optional, Union

from .block import (
    FormBlock, 
    TableBlock, 
    WorkflowBlock, 
    FileBlock, 
    TagBlock, 
    StatBlock, 
    ChartBlock, 
    TextBlock
)

PageBlock = Union[
    FormBlock, 
    TableBlock, 
    WorkflowBlock, 
    FileBlock, 
    TagBlock, 
    StatBlock, 
    ChartBlock, 
    TextBlock
]

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