# business/bookings/ui/pages/booking_create.py

from core.ui.registry import register_ui_module_pages
from core.ui.schema.page import Page
from core.ui.schema.block import BookingBlock

UI_PAGES = Page(
    key="bookings.create",
    domain="business",
    entity="bookings",
    path="/business/bookings/create",
    title="Booking",
    permissions=["business.bookings.create"],
    data_source=None,
    blocks=[
        BookingBlock(
            title="Buat Booking",
            data_source="/business/bookings/context/",
            data_params=["partner_id"],
            estimate_endpoint="/business/bookings/estimate/",
            submit_to="/business/bookings/",
            redirect_to={
                "page": "bookings.detail",
                "param": "id"
            }
        )
    ]
)

register_ui_module_pages("business", UI_PAGES)