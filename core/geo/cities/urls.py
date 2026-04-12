# core/geo/cities/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.geo.cities.views import CityViewSet

router = DefaultRouter()
router.register("cities", CityViewSet, basename="city")

urlpatterns = [
    path("", include(router.urls)),
]