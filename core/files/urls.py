# core/files/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.files.views import FileViewSet

router = DefaultRouter()
router.register("files", FileViewSet, basename="file")

urlpatterns = [
    path("", include(router.urls)),
]
