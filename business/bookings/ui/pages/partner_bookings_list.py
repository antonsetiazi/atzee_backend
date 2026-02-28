# business/bookings/ui/pages/partner_bookings_list.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import ListViewBlock, ListTileSchema, ListFieldSchema
from core.ui.schema.action import Action

from business.enum.permissions import BusinessPermission

UI_PAGES = Page(
    key="partner.bookings.list",
    entity="partner.bookings.schedule",
    domain="business",
    title="My Schedule",
    path="/business/partner/bookings/schedule",
    data_source="/entities/business/partner.bookings.upcoming/query/",
    permissions=[BusinessPermission.PARTNER_BOOKINGS_VIEW],
    blocks=[
        ListViewBlock(
            title="My Schedule",
            data_key="items",  # karena response langsung array
            layout="card",
            tile=ListTileSchema(
                title=ListFieldSchema(
                    key="booking_number"
                ),
                subtitle=ListFieldSchema(
                    key="partner_name"
                ),
                description=ListFieldSchema(
                    key="start_time",
                    format="datetime"
                ),
                trailing=ListFieldSchema(
                    key="partner_amount",
                    format="currency",
                    currency="IDR"
                ),
                status=ListFieldSchema(
                    key="status"
                ),
                meta={
                    "Duration": ListFieldSchema(
                        key="duration_minutes",
                        suffix=" mins"
                    ),
                    "Payment": ListFieldSchema(
                        key="payment_status"
                    ),
                },
                action=Action(
                    type="navigate",
                    label="Detail",
                    to="/business/bookings/{id}/detail",
                    permission="business.user.bookings.view"
                )
            ),
            permissions=["business.partner.bookings.view"],
        )
    ]
)

register_ui_module_pages("business", UI_PAGES)