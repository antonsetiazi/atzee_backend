# hrms/api/attendance/urls.py

from django.urls import path

from .views import (
    CheckInApi,
    CheckOutApi,
    TodayAttendanceApi,
)

urlpatterns = [
    path("", TodayAttendanceApi.as_view(), name="attendance-list"),
    path("check-in/", CheckInApi.as_view(), name="attendance-check-in"),
    path("check-out/", CheckOutApi.as_view(), name="attendance-check-out"),
]
