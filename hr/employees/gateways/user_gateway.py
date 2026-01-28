from uuid import UUID
from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class UserSnapshot:
    """
    Read-only snapshot of Core User.
    HR must NOT mutate this.
    """
    id: UUID
    email: str
    is_active: bool


class UserGateway:
    """
    Gateway interface for Core User.
    """

    def get_user(self, *, user_id: UUID) -> Optional[UserSnapshot]:
        raise NotImplementedError
    
    def ensure_user_is_active(self, *, user_id: UUID) -> None:
        raise NotImplementedError