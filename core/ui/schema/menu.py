from dataclasses import dataclass
from typing import Optional


@dataclass
class Menu:
    key: str
    label: str
    route: str

    app: str
    resource: str
    action: str

    icon: Optional[str] = None
    parent: Optional[str] = None
    order: int = 0
    is_active: bool = True

    def to_dict(self) -> dict:
        return {
            "key": self.key,
            "label": self.label,
            "icon": self.icon,
            "parent": self.parent,
            "app": self.app,
            "resource": self.resource,
            "action": self.action,
            "route": self.route,
            "order": self.order,
            "is_active": self.is_active,
        }
