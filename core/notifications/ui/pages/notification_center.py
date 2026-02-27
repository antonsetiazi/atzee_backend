# core/notifications/ui/pages/notification_center.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    ListViewBlock,
    ListTileSchema,
    ListFieldSchema,
    TextBlock,
)
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="core.notification.center",
    entity="core.notification",
    domain="core",
    title="Notification Center",
    path="/core/notifications",
    permissions=["core.notification.view"],
    data_source="/notifications/",
    method="GET",
    description="View your notifications and system updates",
    blocks=[
        ListViewBlock(
            title="Recent Notifications",
            data_key=None,  # API returns array directly
            layout="card",
            density="comfortable",
            selectable="none",
            value_key="id",
            tile=ListTileSchema(
                title=ListFieldSchema(
                    key="title",
                    icon="notifications"
                ),
                subtitle=ListFieldSchema(
                    key="message"
                ),
                description=ListFieldSchema(
                    key="created_at",
                    format="datetime"
                ),
                status=ListFieldSchema(
                    key="level"
                ),
                # action=Action(
                #     type="navigate",
                #     path="/resolver/entity-link/",  
                #     method="GET",
                #     bind_from_field="entity_id"
                # )
            ),
            permissions=["core.notification.view"],
            empty_title="No notifications yet",
            empty_description="You're all caught up 🎉"
        )
    ]
)

register_ui_module_pages("core", UI_PAGES)