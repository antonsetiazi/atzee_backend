# core/geo/countries/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.geo.countries.views import CountryViewSet

router = DefaultRouter()
router.register("countries", CountryViewSet, basename="country")

urlpatterns = [
    path("", include(router.urls)),
]
