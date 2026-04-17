# business/partners/ui/pages/partner_portal/my_profile.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import (
    ContainerBlock,
    ImageGalleryBlock,
    InfoBlock,
    StatBlock,
    ActionBlock,
)
from core.ui.schema.action import Action

from business.enum.permissions import BusinessPermission

UI_PAGES = Page(
    key="partner_portal.my_profile",
    domain="business",
    entity="partners",
    path="/partner/profile",
    title="My Profile",
    subtitle="Manage your public identity and business information",
    permissions=[BusinessPermission.PARTNERS_PORTAL],
    data_source="/entities/business/partners.me/query/",
    method="POST",
    blocks=[

        # HERO SECTION
        ContainerBlock(
            direction="row",
            gap=24,
            blocks=[

                ImageGalleryBlock(
                    title="Profile Photo",
                    data_key="image_urls",
                    multiple=False,
                    size="lg",
                    max_height=220,
                ),

                ContainerBlock(
                    direction="column",
                    gap=8,
                    blocks=[
                        InfoBlock(
                            key="name",
                            title="Partner Name",
                        ),
                        InfoBlock(
                            key="specialization",
                            title="Specialization",
                        ),
                        InfoBlock(
                            key="location_label",
                            title="Location",
                        ),
                        InfoBlock(
                            key="status_label",
                            title="Status",
                        ),
                    ],
                ),
            ],
        ),

        # QUICK STATS
        ContainerBlock(
            direction="row",
            gap=16,
            blocks=[
                StatBlock(
                    key="rating_avg",
                    data_key="rating_avg",
                    title="Rating",
                    meta={"suffix": "⭐"},
                ),
                StatBlock(
                    key="rating_count",
                    data_key="rating_count",
                    title="Reviews",
                ),
                StatBlock(
                    key="total_bookings",
                    data_key="total_bookings",
                    title="Bookings",
                ),
                StatBlock(
                    key="completed_orders",
                    data_key="completed_orders",
                    title="Completed",
                ),
            ],
        ),

        ContainerBlock(
            direction="row",
            gap=24,
            blocks=[
                ContainerBlock(
                    direction="column",
                    gap=8,
                    blocks=[
                        # ABOUT
                        InfoBlock(
                            title="About Me",
                            key="bio",
                        ),

                        # WORKING HOURS
                        InfoBlock(
                            key="working_hours_label",
                            title="Working Hours",
                        ),
                    ]
                ),

                # CONTACT
                ContainerBlock(
                    direction="column",
                    gap=8,
                    blocks=[
                        InfoBlock(key="phone", title="Phone"),
                        InfoBlock(key="phone", title="Phone"),
                        InfoBlock(key="email", title="Email"),
                        InfoBlock(key="address", title="Address"),
                    ],
                ),
            ]
        ),     

        # ACTIONS
        ActionBlock(
            title="",
            justify="between",
            align="stretch",
            actions=[
                Action(
                    type="navigate",
                    label="Edit Profile",
                    icon="edit",
                    to="/partner/my-profile/edit",
                ),
                Action(
                    type="navigate",
                    label="Manage Services",
                    icon="list",
                    to="/partner/services",
                ),
            ],
        ),
    ],
)

register_ui_module_pages("business", UI_PAGES)