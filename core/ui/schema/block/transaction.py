# core/ui/schema/block/transaction.py

from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class TransactionBlock:
    type: str = "transaction"

    # Presentation
    title: Optional[str] = "Transaction Workspace"
    description: Optional[str] = None

    # 🔥 Single mutation endpoint
    submit_to: Optional[str] = None
    submit_method: str = "POST"

    # Success handling
    redirect_to: Optional[Dict[str, Any]] = None

    # Cache & side effects
    affects: Optional[list[str]] = field(default_factory=list)
    refresh_cache: Optional[list[str]] = field(default_factory=list)

    # Config injection
    config: Dict[str, Any] = field(default_factory=dict)