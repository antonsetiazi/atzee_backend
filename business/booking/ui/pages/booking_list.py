# business/booking/ui/pages/booking_list.py

from core.ui.registry import register_ui_module_pages
from business.booking.ui.pages._base_booking_list import (
    build_booking_list_page,
)

from business.enum.permissions import BusinessPermission


UI_PAGES = build_booking_list_page(
    key="bookings.list",
    domain="business",
    title_page="Bookings",
    subtitle_page="Monitor all booking sessions and schedules",
    path="/admin/bookings",
    data_source="/entities/business/bookings.list/query/",
    permissions=[BusinessPermission.ADMIN_BOOKINGS_VIEW],
    detail_path="/admin/bookings/{id}",
    search_mode="server",
)

register_ui_module_pages("business", UI_PAGES)