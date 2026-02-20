# core/permissions/services.py

from core.permissions.models import Permission

class PermissionService:
    """
    CENTRAL PERMISSION ENGINE
    """

    @staticmethod
    def user_has_permission(*, user, tenant, permission_code: str) -> bool:
        if not user or not user.is_authenticated:
            return False

        return Permission.objects.filter(
            tenant=tenant,
            code=permission_code,
            permission_roles__role__role_users__user=user,
            permission_roles__role__tenant=tenant,
        ).exists()

    @staticmethod
    def user_has_any_permission(*, user, tenant, permission_codes: list[str]) -> bool:
        if not user or not user.is_authenticated:
            return False

        return Permission.objects.filter(
            tenant=tenant,
            code__in=permission_codes,
            permission_roles__role__role_users__user=user,
            permission_roles__role__tenant=tenant,
        ).exists()

    @staticmethod
    def can_access(*, user, tenant, permission_code: str) -> bool:
        if not user or not user.is_authenticated:
            return False

        # PLATFORM OVERRIDE
        if user.is_superuser:
            return True

        return PermissionService.user_has_permission(
            user=user,
            tenant=tenant,
            permission_code=permission_code
        )
