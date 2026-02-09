# core/classifications/tags/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.classifications.tags.views import TagViewSet

router = DefaultRouter()
router.register("tags", TagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
]
