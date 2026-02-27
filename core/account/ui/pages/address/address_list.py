# core/account/ui/pages/address/address_list.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    ListViewBlock,
    ListTileSchema,
    ListFieldSchema,
    ActionBlock,
)
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="core.account.address",
    entity="account.address",
    domain="core",
    title="Address",
    path="/account/address",
    permissions=["core.account.profile.view"],
    data_source="/account/address/",
    method="GET",
    description="Manage your saved addresses for deliveries and billing",
    blocks=[
        ListViewBlock(
            title="My Address",
            data_key=None,  # API returns array directly
            layout="card",
            density="comfortable",
            selectable="none",
            value_key="id",
            tile=ListTileSchema(
                title=ListFieldSchema(
                    key="label",  # Home / Office / etc
                    icon="location_on"
                ),
                subtitle=ListFieldSchema(
                    key="address_line"
                ),
                description=ListFieldSchema(
                    key="city"
                ),
                status=ListFieldSchema(
                    key="country"
                ),
                action=Action(
                    type="navigate",
                    label="Edit",
                    to="/account/address/{id}/edit",
                    permission="core.account.profile.update",
                ),
            ),
            permissions=["core.account.profile.view"],
            empty_title="No saved address",
            empty_description="Add your first address to get started."
        ),

        # 🔹 Add Address Button
        ContainerBlock(
            direction="row",
            justify="center",
            blocks=[
                ActionBlock(
                    actions=[
                        Action(
                            type="navigate",
                            label="Add New Address",
                            icon="add_location",
                            to="/account/address/create",
                            permission="core.account.profile.update"
                        )
                    ],
                    justify="center",
                )
            ]
        )
    ]
)

register_ui_module_pages("core", UI_PAGES)