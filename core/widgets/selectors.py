# core/widgets/selectors.py

from typing import Optional
from django.utils import timezone
from django.db.models import QuerySet, Q

from core.widgets.models import UIWidget
from core.tenants.models import Tenant
from core.users.models import User


def get_widget_queryset(*, tenant: Tenant) -> QuerySet[UIWidget]:
    return UIWidget.objects.filter(
        tenant=tenant,
        is_deleted=False
    )


def get_widgets(*, tenant: Tenant) -> QuerySet[UIWidget]:
    return get_widget_queryset(tenant=tenant)


def get_widget_by_id(*, tenant: Tenant, widget_id: int) -> Optional[UIWidget]:
    try:
        return get_widget_queryset(tenant=tenant).get(id=widget_id)
    except UIWidget.DoesNotExist:
        return None


def get_active_widgets_for_user(
    *,
    tenant: Tenant,
    user: User,
    position: Optional[str] = None,
    current_app: Optional[str] = None,
) -> QuerySet[UIWidget]:

    now = timezone.now()

    qs = get_widget_queryset(tenant=tenant).filter(
        is_active=True
    ).filter(
        Q(starts_at__isnull=True) | Q(starts_at__lte=now)
    ).filter(
        Q(ends_at__isnull=True) | Q(ends_at__gte=now)
    )

    if position:
        qs = qs.filter(position=position)

    widgets = []

    user_roles = []

    if hasattr(user, "roles"):
        user_roles = list(user.roles.values_list("code", flat=True))
        
    if not user_roles:
        user_roles = ["guest"]

    for widget in qs:
        # Role filter
        if widget.target_roles:
            if not any(role in widget.target_roles for role in user_roles):
                continue

        # Permission filter
        if widget.target_permissions:
            user_permissions = user.get_all_permissions()
            if not any(p in user_permissions for p in widget.target_permissions):
                continue

        widgets.append(widget)

    return widgets
