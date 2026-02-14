from typing import Optional
from django.db import transaction
from rest_framework.exceptions import ValidationError

from core.widgets.models import UIWidget
from core.widgets import selectors
from core.tenants.models import Tenant
from core.users.models import User


@transaction.atomic
def create_widget(
    *,
    tenant: Tenant,
    created_by: User,
    **data
) -> UIWidget:

    widget = UIWidget.objects.create(
        tenant=tenant,
        created_by=created_by,
        **data
    )

    return widget


@transaction.atomic
def update_widget(
    *,
    tenant: Tenant,
    widget_id: int,
    updated_by: User,
    **data
) -> UIWidget:

    widget = selectors.get_widget_by_id(
        tenant=tenant,
        widget_id=widget_id
    )

    if not widget:
        raise ValidationError("Widget not found.")

    for field, value in data.items():
        setattr(widget, field, value)

    widget.updated_by = updated_by
    widget.save()

    return widget


@transaction.atomic
def delete_widget(
    *,
    tenant: Tenant,
    widget_id: int,
    deleted_by: User
) -> None:

    widget = selectors.get_widget_by_id(
        tenant=tenant,
        widget_id=widget_id
    )

    if not widget:
        raise ValidationError("Widget not found.")

    widget.is_deleted = True
    widget.updated_by = deleted_by
    widget.save(update_fields=[
        "is_deleted",
        "updated_by",
        "updated_at"
    ])
