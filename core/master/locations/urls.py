# core/master/locations/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.master.locations.views import LocationViewSet


router = DefaultRouter()
router.register(r"locations", LocationViewSet, basename="location")

urlpatterns = [
    path("", include(router.urls)),
]
