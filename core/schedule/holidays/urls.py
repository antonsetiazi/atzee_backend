# core/schedule/holidays/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.schedule.holidays.views import HolidayViewSet

router = DefaultRouter()
router.register(r'holidays', HolidayViewSet, basename='holiday')

urlpatterns = [
    path('', include(router.urls)),
]
