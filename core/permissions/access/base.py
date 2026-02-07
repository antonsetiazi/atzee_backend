# core/permissions/access/base.py

from rest_framework.permissions import BasePermission


class BaseAccessPolicy(BasePermission):
    """
    Base class for domain-based access policies.
    """

    domain: str | None = None
    min_level: tuple[str, ...] = ()

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if getattr(user, "is_superuser", False):
            return True

        role = getattr(user, "role", None)
        if not role:
            return False

        if self.min_level and role.level not in self.min_level:
            return False

        if self.domain:
            apps = role.apps or {}
            domain_cfg = apps.get(self.domain)

            if not domain_cfg:
                return False

            if domain_cfg is True:
                return True

            if isinstance(domain_cfg, dict):
                return domain_cfg.get("enabled", False)

            return False

        return True
