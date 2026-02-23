# business/bookings/ui/pages/partner_bookings_list.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="partner.bookings.list",
    entity="partner.bookings.upcoming",
    domain="business",
    title="Booking Schedule",
    path="/business/partner/bookings",
    permissions=["business.partner.bookings.view"],
    blocks=[
        TableBlock(
            data_source="/entities/business/partner.bookings.upcoming/query/",
            search_mode="server",
            columns=[
                TableColumn(key="booking_number", label="Booking Number", priority=1),
                TableColumn(key="user_name", label="Customer"),
                TableColumn(key="start_time", label="Start Time", type="datetime"),
                TableColumn(key="duration_minutes", label="Duration (mins)"),
                TableColumn(key="partner_amount", label="Earnings", type="currency", align="right"),
                TableColumn(key="status", label="Status"),
                TableColumn(key="payment_status", label="Payment"),
            ],
            actions=[],
            top_actions=[],
            detail_as_state=False,
        )
    ]
)

register_ui_module_pages("business", UI_PAGES)