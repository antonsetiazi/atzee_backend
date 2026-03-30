# business/booking/api/urls.py

from django.urls import path
from .views import (
    CreateBookingHoldAPI,
    ConfirmBookingAPI,
    CancelBookingAPI,
    AvailabilityAPI
)

urlpatterns = [
    path("booking/hold", CreateBookingHoldAPI.as_view()),

    # 🔄 Booking lifecycle
    path("booking/<uuid:booking_id>/confirm", ConfirmBookingAPI.as_view()),
    path("booking/<uuid:booking_id>/cancel", CancelBookingAPI.as_view()),

    # 📅 Availability
    path("booking/availability", AvailabilityAPI.as_view()),
]