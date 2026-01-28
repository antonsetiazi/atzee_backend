from core.audit_logs.models import AuditLog
from core.audit_logs.context import (
    set_current_user,
    clear_current_user,
)


class AuditMiddleware:
    """
    Capture request-level audit information
    and provide user context for model-level audit.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ============================
        # BEFORE REQUEST (SET CONTEXT)
        # ============================
        if request.user.is_authenticated:
            set_current_user(request.user)

        try:
            response = self.get_response(request)
        finally:
            # ============================
            # AFTER REQUEST (CLEAR CONTEXT)
            # ============================
            clear_current_user()

        # ============================
        # REQUEST-LEVEL AUDIT LOG
        # ============================
        if not hasattr(request, "tenant"):
            return response

        if not request.user.is_authenticated:
            return response

        AuditLog.objects.create(
            tenant=request.tenant,
            user=request.user,
            action="http_request",
            resource=request.path,
            metadata={
                "method": request.method,
                "status_code": response.status_code,
            },
        )

        return response
