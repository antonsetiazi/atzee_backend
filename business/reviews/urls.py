# business/reviews/urls.py

from django.urls import path
from .views import (
    CreateReviewAPI,
    PartnerReviewListAPI,
    BookingReviewDetailAPI
)

urlpatterns = [
    path("reviews/", CreateReviewAPI.as_view()),
    path("reviews/partner/<int:partner_id>/", PartnerReviewListAPI.as_view()),
    path("reviews/booking/<int:booking_id>/", BookingReviewDetailAPI.as_view()
),
]