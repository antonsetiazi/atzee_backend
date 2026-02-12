# core/schedule/recurrings/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.schedule.recurrings.views import RecurringViewSet

router = DefaultRouter()
router.register(r"recurrings", RecurringViewSet, basename="recurring")

urlpatterns = [
    path("", include(router.urls)),
]
