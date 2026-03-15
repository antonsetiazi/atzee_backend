# core/roles/middleware.py

from core.roles.models import Role


class RoleContextMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        role_id = request.headers.get("X-Role-Id")
   
        if role_id:
            try:
                role = Role.objects.get(
                    id=role_id,
                    tenant=request.tenant
                )
                request.role = role
            except Role.DoesNotExist:
                request.role = None

        return self.get_response(request)