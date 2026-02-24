# business/bookings/ui/pages/user_bookings_history.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import ListViewBlock, ListTileSchema, ListFieldSchema
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="user.bookings.history",
    entity="user.bookings.history",
    domain="business",
    title="My Bookings",
    path="/business/my-bookings",
    permissions=["business.user.bookings.view"],
    data_source="/entities/business/user.bookings.history/query/",
    method="POST",
    blocks=[
        ListViewBlock(
            title="Booking History",
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
                    key="total_price",
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
            permissions=["business.user.bookings.view"],
        )
    ]
)

register_ui_module_pages("business", UI_PAGES)