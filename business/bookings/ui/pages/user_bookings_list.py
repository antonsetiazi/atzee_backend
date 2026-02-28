# business/bookings/ui/pages/user_bookings_list.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action

from business.enum.permissions import BusinessPermission


UI_PAGES = Page(
    key="user.bookings.list",
    entity="user.bookings.upcoming",
    domain="business",
    title="My Bookings",
    path="/business/user/bookings/schedule",
    permissions=[BusinessPermission.USER_BOOKINGS_VIEW],
    blocks=[
        TableBlock(
            data_source="/entities/business/user.bookings.upcoming/query/",
            search_mode="server",
            columns=[
                TableColumn(key="booking_number", label="Booking Number", priority=1),
                TableColumn(key="partner_name", label="Partner"),
                TableColumn(key="start_time", label="Start Time", type="datetime"),
                TableColumn(key="duration_minutes", label="Duration (mins)"),
                TableColumn(key="total_price", label="Total Price", type="currency", align="right"),
                TableColumn(key="status", label="Status"),
                TableColumn(key="payment_status", label="Payment"),
            ],
            actions=[
                Action(
                    type="redirect",
                    label="Detail",
                    to="/business/bookings/{id}/detail",
                )
            ],
            top_actions=[],
            detail_as_state=False,
        )
    ]
)

register_ui_module_pages("business", UI_PAGES)