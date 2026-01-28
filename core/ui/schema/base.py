# core/ui/schema/base.py

from dataclasses import dataclass, field
from typing import List, Optional, Literal


HTTPMethod = Literal["GET", "POST", "PATCH", "DELETE"]