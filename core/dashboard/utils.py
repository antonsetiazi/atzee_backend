# core/dashboard/utils.py

from .services import DashboardService


def resolve_service(path: str):
    """
    path: "dashboard.total_users"
    """
    parts = path.split(".")
    method_name = parts[-1]

    service = getattr(DashboardService, method_name, None)

    if not service:
        raise ValueError(f"Dashboard service '{path}' not found")

    return service
