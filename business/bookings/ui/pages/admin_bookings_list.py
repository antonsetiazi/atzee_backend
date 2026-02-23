# business/bookings/ui/pages/admin_bookings_list.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import TableBlock, TableColumn
from core.ui.schema.action import Action


UI_PAGES = Page(
    key="admin.bookings.list",
    entity="admin.bookings.list",
    domain="business",
    title="All Bookings",
    path="/business/admin/bookings",
    permissions=["business.admin.bookings.view"],
    blocks=[
        TableBlock(
            data_source="/entities/business/admin.bookings.list/query/",
            search_mode="server",
            columns=[
                TableColumn(key="booking_number", label="Booking Number", priority=1),
                TableColumn(key="user_name", label="Customer"),
                TableColumn(key="partner_name", label="Partner"),
                TableColumn(key="start_time", label="Start Time", type="datetime"),
                TableColumn(key="total_price", label="Total Price", type="currency", align="right"),
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