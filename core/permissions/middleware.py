from django.core.exceptions import PermissionDenied
from core.permissions.services import PermissionService


class PermissionGuardMiddleware:
    """
    Enforce permission if view declares required_permission.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        required_permission = getattr(
            view_func,
            "required_permission",
            None
        )

        if not required_permission:
            return None

        if not request.tenant:
            raise PermissionDenied("Tenant context required")

        if not PermissionService.can_access(
            user=request.user,
            tenant=request.tenant,
            permission_code=required_permission
        ):
            raise PermissionDenied(
                f"Permission '{required_permission}' required"
            )

        return None
