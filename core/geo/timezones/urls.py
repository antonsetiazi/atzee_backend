# core/geo/timezones/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.geo.timezones.views import TimezoneViewSet

router = DefaultRouter()
router.register("timezones", TimezoneViewSet, basename="timezone")

urlpatterns = [
    path("", include(router.urls)),
]
