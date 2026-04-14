# business/reviews/ui/pages/review_list.py

from core.ui.registry import register_ui_module_pages
from business.reviews.ui.pages._base_review_list import (
    build_review_list_page,
)

from business.enum.permissions import BusinessPermission


UI_PAGES = build_review_list_page(
    key="reviews.list",
    domain="business",
    title_page="Reviews",
    subtitle_page="Monitor user feedback and partner ratings",
    path="/admin/reviews",
    data_source="/entities/business/reviews.list/query/",
    permissions=[BusinessPermission.ADMIN_REVIEWS_VIEW],
    detail_path="/admin/reviews/{id}",
    search_mode="server",
)

register_ui_module_pages("business", UI_PAGES)