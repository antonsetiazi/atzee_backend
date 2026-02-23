# core/ui/schema/block/booking.py

from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List


@dataclass
class BookingBlock:
    """
    Composite block representing full booking workflow.

    Flow:
    1. Load booking context (GET)
    2. Optional estimate calculation (POST)
    3. Commit booking (POST)
    """

    # block identity
    type: str = "booking"

    # presentation
    title: Optional[str] = "Buat Booking"
    description: Optional[str] = None
    layout: str = "vertical"

    # =========================
    # 1️⃣ CONTEXT (READ)
    # =========================
    data_source: Optional[str] = None
    data_method: str = "GET"
    data_params: Optional[List[str]] = field(default_factory=list)

    # =========================
    # 2️⃣ ESTIMATE (CALCULATION)
    # =========================
    estimate_endpoint: Optional[str] = None
    estimate_method: str = "POST"

    # =========================
    # 3️⃣ COMMIT (STATE MUTATION)
    # =========================
    submit_to: Optional[str] = None
    submit_method: str = "POST"

    # =========================
    # SUCCESS HANDLING
    # =========================
    redirect_to: Optional[Dict[str, Any]] = None

    # =========================
    # WORKFLOW CONFIG
    # =========================
    allow_multiple_services: bool = True
    require_schedule: bool = True
    require_notes: bool = False

    # =========================
    # EXTENSIBLE CONFIG
    # =========================
    config: Dict[str, Any] = field(default_factory=dict)